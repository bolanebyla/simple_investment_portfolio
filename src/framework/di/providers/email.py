from dishka import Provider, Scope, provide

from investment_portfolio.application.interfaces import EmailSender
from investment_portfolio.infrastructure.email.senders import (
    EmailSenderImpl,
)


class EmailProvider(Provider):
    scope = Scope.APP

    email_sender = provide(
        EmailSenderImpl,
        provides=EmailSender,
    )
