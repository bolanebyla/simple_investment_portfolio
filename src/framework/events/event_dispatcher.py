from typing import Callable

from investment_portfolio.application.application_events import (
    BaseApplicationEvent,
)
from investment_portfolio.application.interfaces import EventDispatcher
from investment_portfolio.domain.domain_events import BaseDomainEvent

EventAlias = BaseDomainEvent | BaseApplicationEvent
HandlerAlias = Callable[[EventAlias], None]


class EventDispatcherImpl(EventDispatcher):
    # TODO: не потокобезопасно
    _handlers: dict[type[EventAlias], list[HandlerAlias]]

    def __init__(self):
        self._handlers = {}

    def register_handler(
        self,
        event_type: type[EventAlias],
        handler: HandlerAlias,
    ) -> None:
        self._handlers.setdefault(event_type, []).append(handler)

    def dispatch(self, event: EventAlias) -> None:
        event_type = type(event)

        handlers = self._handlers.get(event_type, [])

        for handler in handlers:
            handler(event)
