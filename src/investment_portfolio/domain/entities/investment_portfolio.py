from dataclasses import dataclass
from uuid import UUID

from investment_portfolio.domain.domain_events import (
    InvestmentPortfolioCreatedEvent,
)
from investment_portfolio.domain.entities.base import BaseEntity


@dataclass(kw_only=True)
class InvestmentPortfolio(BaseEntity):
    """
    Инвестиционный портфель
    """

    def __post_init__(self):
        created_event = InvestmentPortfolioCreatedEvent(
            investment_portfolio_id=self.id
        )
        self._add_domain_event(created_event)

    id: UUID
    title: str
