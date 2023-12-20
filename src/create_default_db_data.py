import contextlib
import os

import django
from django.conf import settings

from dotenv import find_dotenv, load_dotenv

os.environ["DJANGO_SETTINGS_MODULE"] = "proj.settings"

load_dotenv(find_dotenv())

if not settings.configured:
    django.setup()

from catalog.models import AppUser


def create_superuser_for_adminpanel():
    AppUser.objects.create_superuser(
        username=os.getenv("DJANGO_SUPERUSER_USERNAME"),
        password=os.getenv("DJANGO_SUPERUSER_PASSWORD"),
    )


if __name__ == "__main__":
    with contextlib.suppress(django.db.utils.IntegrityError):
        create_superuser_for_adminpanel()
