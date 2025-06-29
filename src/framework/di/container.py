from dishka import make_container

from framework.di.providers import DBRepositoriesProvider, UseCasesProvider

container = make_container(
    DBRepositoriesProvider(),
    UseCasesProvider(),
)
