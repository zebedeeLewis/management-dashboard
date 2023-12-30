import os
from django.urls import path, include

DEFAULT_API_ROOT = 'api'
api_root = os.environ.setdefault('API_ROOT', DEFAULT_API_ROOT)

urlpatterns = [
    path(api_root + '/', include('api.urls')),
]
