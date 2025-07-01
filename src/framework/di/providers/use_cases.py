from dishka import Provider, Scope, provide

from investment_portfolio.application.use_cases import (
    CreateUserInvestmentPortfolioUseCase,
    SendFirstUserPortfolioCreatedEmailUseCase,
)


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    create_user_investment_portfolio = provide(
        CreateUserInvestmentPortfolioUseCase,
    )

    sent_first_user_portfolio_created_email_use_case = provide(
        SendFirstUserPortfolioCreatedEmailUseCase,
    )
