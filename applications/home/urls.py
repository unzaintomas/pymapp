# home/urls.py
from django.urls import path
from .views import dashboard_view, user_login, user_logout

app_name = "home_app"

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]