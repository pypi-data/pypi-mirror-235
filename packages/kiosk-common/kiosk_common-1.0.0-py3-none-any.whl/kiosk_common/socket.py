from __future__ import annotations

import json
import logging
import struct
from dataclasses import dataclass
from socket import socket, MSG_PEEK
from typing import Any


@dataclass(frozen=True)
class PacketHeader:
    length: int

    @staticmethod
    def parse(buff: bytes) -> PacketHeader:
        if len(buff) != 8:
            raise BadPacketHeader(buff)

        magic, length = struct.unpack('!2sxxI', buff)
        if magic != b'IW':
            raise BadPacketHeader(buff)

        return PacketHeader(length=length)

    def to_bytes(self) -> bytes:
        return struct.pack('!2sxxI', b'IW', self.length)


@dataclass(frozen=True)
class Packet:
    header: PacketHeader
    body: bytes

    def to_bytes(self) -> bytes:
        return self.header.to_bytes() + self.body


class BadPacketHeader(ValueError):
    ...


def socket_recv_header(sock: socket, peek: bool = False) -> PacketHeader:
    flags = MSG_PEEK if peek else 0
    return PacketHeader.parse(sock.recv(8, flags))


def socket_recv_packet(sock: socket, peek: bool = False) -> Packet:
    flags = MSG_PEEK if peek else 0

    header = socket_recv_header(sock, peek)
    body = sock.recv(8 + header.length if peek else header.length, flags)

    if peek:
        body = body[8:]

    packet = Packet(header=header, body=body)
    logging.debug(f'{"peek" if peek else "recv"} packet: %s from %s', packet.to_bytes(), sock.getpeername())

    return packet


def socket_recv_json(sock: socket, peek: bool = False) -> Any:
    packet = socket_recv_packet(sock, peek)

    return json.loads(packet.body.decode('utf-8'))


def socket_send_packet(sock: socket, body: bytes):
    header = PacketHeader(length=len(body))
    buff = header.to_bytes() + body
    logging.debug('send packet: %s to %s', buff, sock.getpeername())
    sock.send(buff)


def socket_send_json(sock: socket, data: Any):
    socket_send_packet(sock, json.dumps(data).encode('utf-8'))
