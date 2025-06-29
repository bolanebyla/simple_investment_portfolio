from dishka import Provider, Scope, provide

from investment_portfolio.domain.repositories import InvestmentPortfolioRepo
from investment_portfolio.infrastructure.repositories import (
    InvestmentPortfolioRepoImpl,
)


class DBRepositoriesProvider(Provider):
    scope = Scope.REQUEST

    investment_portfolio_repo = provide(
        InvestmentPortfolioRepoImpl,
        provides=InvestmentPortfolioRepo,
    )
