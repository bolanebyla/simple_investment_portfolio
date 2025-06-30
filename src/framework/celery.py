import os
import platform

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework.settings")

celery_app = Celery("framework")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Windows-specific configuration
if platform.system().lower() == "windows":
    # Force the use of threads pool on Windows
    celery_app.conf.update(
        worker_pool="threads",
        worker_concurrency=4,
        task_always_eager=False,
        worker_prefetch_multiplier=1,
        worker_pool_restarts=True,
    )

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()
