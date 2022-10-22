from .base import *
from typing import Optional
import os
from typing import Optional, Union
import environ

env = environ.Env(DEBUG=(bool, True))

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")


ALLOWED_HOSTS: Optional[list] = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_ADDRESS = "enowblog@gmail.com"
