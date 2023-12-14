from django.urls import path, include

urlpatterns = [
    path('api/', include('app_api.urls')),
]
