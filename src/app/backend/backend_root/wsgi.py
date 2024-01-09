"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

APPS_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = APPS_DIR.parent.parent

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_root.settings')
os.environ.setdefault('PROJECT_DIR', str(PROJECT_DIR))

application = get_wsgi_application()
