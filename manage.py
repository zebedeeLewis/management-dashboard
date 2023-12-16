#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
APP_ROOT = PROJECT_ROOT / 'src/app'

def main():
    """Run administrative tasks."""
    sys.path.append(str(APP_ROOT))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project_root.settings')
    os.environ.setdefault('PROJECT_ROOT', str(PROJECT_ROOT))
    os.environ.setdefault('DEVELOPMENT', 'development')
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
