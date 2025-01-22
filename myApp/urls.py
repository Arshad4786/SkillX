from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Route the root URL to the `home` view
    path('register/', views.register_talent, name='register_talent'),  # Route to the `register_talent` view
        path('login/', auth_views.LoginView.as_view(), name='login'),
         path('talents/', views.talent_list, name='talent_list'),
    path('hire-request/<int:talent_id>/', views.hire_request, name='hire_request'),
    path('client/', views.client_view, name='client_view'),

]
