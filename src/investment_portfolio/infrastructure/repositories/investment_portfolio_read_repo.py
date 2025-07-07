from uuid import UUID

from investment_portfolio.application.dto import UserInvestmentPortfolioDto
from investment_portfolio.application.interfaces import (
    InvestmentPortfolioReadRepo,
)


class InvestmentPortfolioReadRepoImpl(InvestmentPortfolioReadRepo):
    def get_user_investment_portfolio(
        self,
        investment_portfolio_id: UUID,
        user_id: int,
    ) -> UserInvestmentPortfolioDto:
        return UserInvestmentPortfolioDto()
