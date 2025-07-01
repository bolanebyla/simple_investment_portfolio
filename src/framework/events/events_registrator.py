from framework.events.event_dispatcher import EventDispatcherImpl
from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)
from investment_portfolio.infrastructure.tasks import (
    send_first_user_portfolio_created_email,
)


class EventsRegistrator:
    def register_events(self, event_dispatcher: EventDispatcherImpl):
        event_dispatcher.register_handler(
            event_type=FirstUserPortfolioCreatedEvent,
            handler=lambda event: send_first_user_portfolio_created_email.delay_on_commit(
                investment_portfolio_id=event.investment_portfolio_id,
            ),
        )
