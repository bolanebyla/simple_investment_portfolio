from abc import abstractmethod
from typing import Protocol

from investment_portfolio.application.application_events import (
    BaseApplicationEvent,
)
from investment_portfolio.domain.domain_events import BaseDomainEvent


class EventDispatcher(Protocol):
    @abstractmethod
    def dispatch(
        self,
        event: BaseDomainEvent | BaseApplicationEvent,
    ) -> None: ...
