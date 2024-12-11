from django.urls import path
from django.views.generic import TemplateView

from users.views import register_user, login_user


urlpatterns = [
    path('register', register_user, name='register'),
    path('login', login_user, name='login'),
]
