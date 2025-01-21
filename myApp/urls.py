from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route the root URL to the `home` view
    path('register/', views.register_talent, name='register_talent'),  # Route to the `register_talent` view
]
