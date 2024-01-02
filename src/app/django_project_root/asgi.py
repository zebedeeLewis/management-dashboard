"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from pathlib import Path

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'django_project_root.settings')
os.environ.setdefault('PROJECT_DIR',
                      str(Path(__file__).resolve().parent.parent))

application = get_asgi_application()
