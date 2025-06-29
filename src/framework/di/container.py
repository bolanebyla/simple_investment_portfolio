from dishka import make_container

from framework.di.providers import (
    DBRepositoriesProvider,
    EventDispatchersProvider,
    UseCasesProvider,
)

container = make_container(
    DBRepositoriesProvider(),
    UseCasesProvider(),
    EventDispatchersProvider(),
)
