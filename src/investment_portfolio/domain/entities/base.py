from dataclasses import dataclass, field

from investment_portfolio.domain.domain_events import (
    BaseDomainEvent,
)


@dataclass
class BaseEntity:
    __domain_events: list[BaseDomainEvent] = field(default_factory=list)

    def _add_domain_event(self, event):
        self.__domain_events.append(event)

    @property
    def domain_events(self) -> list[BaseDomainEvent]:
        return self.__domain_events
