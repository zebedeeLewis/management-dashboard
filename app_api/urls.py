from django.urls import path
from app_api import views

urlpatterns = [
    path('samples/', views.sample_list),
    path('samples/<int:pk>/', views.sample_detail),
]
