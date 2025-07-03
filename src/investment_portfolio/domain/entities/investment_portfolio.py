from dataclasses import dataclass, field

from investment_portfolio.application.errors import (
    InvestmentPortfolioAlreadyHasAssetWithTicket,
)
from investment_portfolio.domain.domain_events import (
    InvestmentPortfolioCreatedEvent,
)

from .base import BaseEntity
from .investment_asset import InvestmentAsset


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

    title: str
    user_id: int

    assets: list[InvestmentAsset] = field(default_factory=list)

    def add_asset(self, asset: InvestmentAsset) -> None:
        """Добавляет актив в портфель"""
        if self.has_asset_by_ticket(asset.ticket):
            raise InvestmentPortfolioAlreadyHasAssetWithTicket()

        self.assets.append(asset)

    def has_asset_by_ticket(self, asset_ticket: str) -> bool:
        """Проверяет, есть ли в портфеле актив с тикетом"""
        return any(asset.ticket == asset_ticket for asset in self.assets)
