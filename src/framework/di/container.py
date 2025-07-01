from dishka import make_container
from dishka.integrations.celery import setup_dishka

from framework import celery_app
from framework.di.providers import (
    DBRepositoriesProvider,
    EmailProvider,
    EventDispatchersProvider,
    UseCasesProvider,
)

container = make_container(
    DBRepositoriesProvider(),
    UseCasesProvider(),
    EventDispatchersProvider(),
    EmailProvider(),
)


setup_dishka(container=container, app=celery_app)
