from dishka import Provider, Scope, provide

from investment_portfolio.infrastructure.email.senders import (
    FirstUserPortfolioCreatedSender,
)


class EmailProvider(Provider):
    scope = Scope.APP

    first_user_portfolio_created_sender = provide(
        FirstUserPortfolioCreatedSender
    )
