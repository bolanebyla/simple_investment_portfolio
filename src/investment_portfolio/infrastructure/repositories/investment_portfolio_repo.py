from investment_portfolio.domain import InvestmentPortfolio
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo
from investment_portfolio.infrastructure.models import InvestmentPortfolioModel


class InvestmentPortfolioRepoImpl(InvestmentPortfolioRepo):
    def add(self, investment_portfolio: InvestmentPortfolio) -> None:
        InvestmentPortfolioModel.objects.create(
            id=investment_portfolio.id, title=investment_portfolio.title
        )
