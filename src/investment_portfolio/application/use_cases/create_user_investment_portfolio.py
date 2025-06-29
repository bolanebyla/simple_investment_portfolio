import uuid

from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo


class CreateUserInvestmentPortfolioUseCase:
    def __init__(self, investment_portfolio_repo: InvestmentPortfolioRepo):
        self._investment_portfolio_repo = investment_portfolio_repo

    def execute(self) -> None:
        investment_portfolio = InvestmentPortfolio(
            id=uuid.uuid4(),
            title="test",
        )
        self._investment_portfolio_repo.add(
            investment_portfolio=investment_portfolio
        )
