from framework.events.event_dispatcher import EventDispatcherImpl
from investment_portfolio.application.application_events import (
    FirstUserPortfolioCreatedEvent,
)


def mock_send_email(event):
    print("Email sent :", event)


class EventsRegistrator:
    def __init__(
        self,
    ) -> None:
        pass

    def register_events(self, event_dispatcher: EventDispatcherImpl):
        event_dispatcher.register_handler(
            event_type=FirstUserPortfolioCreatedEvent,
            handler=mock_send_email,
        )
