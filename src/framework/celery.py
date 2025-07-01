import os

from celery import Celery, current_app
from celery.contrib.django.task import DjangoTask
from celery.signals import worker_process_shutdown
from dishka import Container
from dishka.integrations.celery import DishkaTask

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework.settings")


class DishkaDjangoTask(DjangoTask, DishkaTask):
    pass


celery_app = Celery(
    "framework",
    task_cls=DishkaDjangoTask,
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()


# TODO: не срабатывает
@worker_process_shutdown.connect()
def close_dishka(*args, **kwargs):
    container: Container = current_app.conf["dishka_container"]
    container.close()
    # TODO: лог
    print("Dishka контейнер закрыт")
