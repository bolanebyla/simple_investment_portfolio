from dishka import Provider, Scope, provide

from investment_portfolio.application.interfaces import (
    InvestmentPortfolioReadRepo,
)
from investment_portfolio.domain.repositories import InvestmentPortfolioRepo
from investment_portfolio.infrastructure.repositories import (
    InvestmentPortfolioReadRepoImpl,
    InvestmentPortfolioRepoImpl,
)


class DBRepositoriesProvider(Provider):
    scope = Scope.REQUEST

    investment_portfolio_repo = provide(
        InvestmentPortfolioRepoImpl,
        provides=InvestmentPortfolioRepo,
    )

    investment_portfolio_read_repo = provide(
        InvestmentPortfolioReadRepoImpl,
        provides=InvestmentPortfolioReadRepo,
    )
