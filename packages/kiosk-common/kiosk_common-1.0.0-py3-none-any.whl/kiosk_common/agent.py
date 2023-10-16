from __future__ import annotations

import logging
import time
from dataclasses import dataclass
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_KEEPALIVE
from socketserver import BaseRequestHandler
from threading import Thread
from typing import Optional, Type, TypedDict, TypeVar, Tuple, Union

from kiosk_common.emitter import Emitter
from .socket import BadPacketHeader, socket_recv_json, socket_send_json

ERROR_BAD_REQUEST = 400
ERROR_NOT_FOUND = 404
ERROR_METHOD_NOT_ALLOWED = 405
ERROR_REQUEST_TIMEOUT = 408
ERROR_INTERNAL_SERVER_ERROR = 500


@dataclass
class Message(TypedDict):
    type: str
    content: TypedDict


@dataclass
class MessageContent:
    ...


@dataclass
class ActionRequest(MessageContent):
    action: str
    arguments: Optional[dict]


@dataclass
class ActionResult(MessageContent):
    action: str
    data: dict


@dataclass
class ActionError(MessageContent):
    code: int
    message: str


@dataclass
class Notification(MessageContent):
    event: str
    data: dict


@dataclass
class AgentException(Exception):
    code: int
    message: str


T = TypeVar("T")


def socket_send_message(sock: socket, content: Union[ActionRequest, ActionResult, ActionError, Notification]):
    socket_send_json(sock, {'type': content.__class__.__name__, 'content': content.__dict__})


def socket_recv_message(sock: socket, types: Tuple[Type[MessageContent], ...]) -> T:
    type_names = [t.__name__ for t in types]

    while True:
        msg = socket_recv_json(sock, peek=True)

        if msg['type'] not in type_names:
            time.sleep(1)
            continue

        msg = socket_recv_json(sock)

        return types[type_names.index(msg['type'])](**msg['content'])


class AgentRequestHandler(BaseRequestHandler):
    request: socket
    alive: bool

    def handle(self):
        logging.debug('Connected from %s', self.request)
        self.alive = True

        while self.alive:
            try:
                req = self.recv_action_request()

                method_name = f'action_{req.action.replace("-", "_")}'

                if not hasattr(self, method_name):
                    raise AgentException(code=ERROR_NOT_FOUND, message=f'Action "{req.action}" not found.')

                self.send_action_result(req.action, getattr(self, method_name)({} if req.arguments is None else req.arguments))
            except (ConnectionResetError, BadPacketHeader):
                break
            except AgentException as exc:
                self.send_action_error(exc.code, exc.message)

    def recv_action_request(self) -> ActionRequest:
        return socket_recv_message(self.request, (ActionRequest,))

    def send_action_result(self, action: str, data: Optional[dict] = None):
        socket_send_message(self.request, ActionResult(action, {} if data is None else data))

    def send_action_error(self, code: int, message: str):
        socket_send_message(self.request, ActionError(code, message))

    def send_notification(self, event: str, data: Optional[dict] = None):
        socket_send_message(self.request, Notification(event, {} if data is None else data))


class AgentClient(Emitter):
    socket: socket

    def __init__(self):
        super().__init__()
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)

    def connect(self, address: Tuple[str, int]):
        logging.debug('Connecting to agent server: %s', address)

        self.socket.connect(address)

        Thread(target=self.thread_notification_monitor).start()

    def thread_notification_monitor(self):
        while True:
            res = socket_recv_message(self.socket, (Notification,))
            self.emit('notification', res)

    def send_request(self, action: str, arguments: Optional[dict] = None) -> ActionResult:
        socket_send_message(self.socket, ActionRequest(action, {} if arguments is None else arguments))

        msg = socket_recv_message(self.socket, (ActionResult, ActionError))

        if isinstance(msg, ActionError):
            raise AgentException(**msg.__dict__)

        return msg
