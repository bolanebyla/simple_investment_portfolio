from dishka import Provider, Scope, provide

from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    create_user_investment_portfolio = provide(
        CreateUserInvestmentPortfolioUseCase,
    )
