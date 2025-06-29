from abc import ABC
from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class BaseApplicationEvent(ABC):
    pass


@dataclass(frozen=True)
class FirstUserPortfolioCreatedEvent(BaseApplicationEvent):
    investment_portfolio_id: UUID
