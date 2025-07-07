from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from investment_portfolio.application.dto import UserInvestmentPortfolioDto


class InvestmentPortfolioReadRepo(Protocol):
    @abstractmethod
    def get_user_investment_portfolio(
        self,
        investment_portfolio_id: UUID,
        user_id: int,
    ) -> UserInvestmentPortfolioDto: ...
