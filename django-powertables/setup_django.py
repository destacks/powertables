import os
from pathlib import Path

import django
from django.conf import settings

BASE_DIR = Path(__file__).resolve().parent


def setup_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        DEBUG=True,
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "powertables",
            "tests",
        ],
    )
    django.setup()
