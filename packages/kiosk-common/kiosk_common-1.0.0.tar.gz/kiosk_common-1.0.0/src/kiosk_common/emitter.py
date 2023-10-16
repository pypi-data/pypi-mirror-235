from abc import ABC
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, TypeAlias


@dataclass
class Event:
    name: str
    target: Any


EventListener: TypeAlias = Callable[[Event, Any], None]


class Emitter(ABC):
    listeners: Dict[str, List[EventListener]]

    def __init__(self):
        self.listeners = {}

    def on(self, event: str, listener: EventListener):
        if event not in self.listeners:
            self.listeners[event] = []

        self.listeners[event].append(listener)

    def emit(self, event: str, *args) -> bool:
        if event not in self.listeners:
            return False

        result = True
        for listener in self.listeners[event]:
            listener_result = listener(Event(name=event, target=self), *args)

            if listener_result is None:
                continue

            result = result and listener_result

            if not result:
                break

        return result
