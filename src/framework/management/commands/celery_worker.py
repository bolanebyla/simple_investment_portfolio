import sys

from django.core.management.base import BaseCommand

PROJECT_NAME = "framework"


class Command(BaseCommand):
    help = "Starts the Celery worker"

    def add_arguments(self, parser):
        parser.add_argument("--loglevel", default="INFO", help="Logging level")
        parser.add_argument(
            "--pool", default="prefork", help="Pool implementation"
        )

    def handle(self, *args, **options):
        from celery.bin import celery as celery_bin

        # Сохраняем оригинальные sys.argv
        orig_argv = sys.argv.copy()
        try:
            sys.argv = [
                "manage.py",
                "-A",
                PROJECT_NAME,
                "worker",
                f"--loglevel={options['loglevel']}",
                f"--pool={options['pool']}",
            ]
            celery_bin.main()
        finally:
            sys.argv = orig_argv
