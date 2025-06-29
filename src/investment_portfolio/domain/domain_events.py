from abc import ABC
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class BaseDomainEvent(ABC):
    pass


@dataclass(frozen=True)
class InvestmentPortfolioCreatedEvent(BaseDomainEvent):
    investment_portfolio_id: UUID
