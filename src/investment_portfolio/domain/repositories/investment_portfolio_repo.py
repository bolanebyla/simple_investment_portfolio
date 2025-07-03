from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from investment_portfolio.domain import InvestmentPortfolio


class InvestmentPortfolioRepo(Protocol):
    @abstractmethod
    def add(self, investment_portfolio: InvestmentPortfolio) -> None: ...

    @abstractmethod
    def get_by_id_and_user_id(
        self,
        id_: UUID,
        user_id: int,
    ) -> InvestmentPortfolio | None: ...
