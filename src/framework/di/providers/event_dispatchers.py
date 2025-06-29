from dishka import Provider, Scope, provide

from framework.events.event_dispatcher import EventDispatcherImpl
from framework.events.events_registrator import EventsRegistrator
from investment_portfolio.application.interfaces import EventDispatcher


class EventDispatchersProvider(Provider):
    scope = Scope.APP

    events_registrator = provide(EventsRegistrator)

    @provide
    def create_event_dispatcher(
        self, events_registrator: EventsRegistrator
    ) -> EventDispatcher:
        event_dispatcher = EventDispatcherImpl()

        events_registrator.register_events(event_dispatcher=event_dispatcher)
        return event_dispatcher
