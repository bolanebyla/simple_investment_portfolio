from framework.events.event_dispatcher import EventDispatcherImpl
from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)
from investment_portfolio.infrastructure.email.senders import (
    FirstUserPortfolioCreatedSender,
)
from investment_portfolio.infrastructure.tasks import (
    send_first_user_portfolio_created_email,
)


class EventsRegistrator:
    def __init__(
        self,
        first_user_portfolio_created_sender: FirstUserPortfolioCreatedSender,
    ) -> None:
        self._first_user_portfolio_created_sender = (
            first_user_portfolio_created_sender
        )

    def register_events(self, event_dispatcher: EventDispatcherImpl):
        # TODO: убрать синхронную отправку
        event_dispatcher.register_handler(
            event_type=FirstUserPortfolioCreatedEvent,
            handler=lambda event: self._first_user_portfolio_created_sender.send(),
        )

        event_dispatcher.register_handler(
            event_type=FirstUserPortfolioCreatedEvent,
            handler=lambda event: send_first_user_portfolio_created_email.delay_on_commit(),
        )
