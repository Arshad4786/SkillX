from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import hire_request



urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_talent, name='register_talent'),
    path('talents/', views.talent_list, name='talent_list'),
    path('client/', views.client_view, name='client_view'),
    path('hire_request/<int:talent_id>/', views.hire_request, name='send_hire_request'),
    path('signin/', views.client_signin, name='client_signin'),
    path('signup/', views.client_signup, name='client_signup'),
]

