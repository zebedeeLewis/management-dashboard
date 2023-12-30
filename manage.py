#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from django.core.management.commands.runserver import Command as runserver
from dotenv import load_dotenv

APP_ROOT = Path(__file__).resolve().parent / 'src/app'

def main():
    """Run administrative tasks."""
    load_dotenv()

    sys.path.append(str(APP_ROOT))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'django_project_root.settings')
    os.environ.setdefault('PROJECT_DIR',
                          str(Path(__file__).resolve().parent))
    runserver.default_port = os.environ.get('PORT') or 8000
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
