"""
Скрипт для запуска Celery worker на Windows
"""

import os
import sys
from pathlib import Path

import django

# Добавляем путь к проекту
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

# Настраиваем Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework.settings")
django.setup()

from celery.bin.celery import main as celery_main

if __name__ == "__main__":
    # Параметры для Windows
    sys.argv = [
        "celery",
        "-A",
        "framework.celery",
        "worker",
        "--pool=threads",
        "--concurrency=4",
        "--loglevel=info",
        "--without-gossip",
        "--without-mingle",
        "--without-heartbeat",
    ]

    print("Запуск Celery worker для Windows...")
    print(f"Команда: {' '.join(sys.argv)}")

    try:
        celery_main()
    except KeyboardInterrupt:
        print("\nОстановка Celery worker...")
    except Exception as e:
        print(f"Ошибка при запуске Celery worker: {e}")
        sys.exit(1)
