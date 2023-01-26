from django.urls import path

from . import views

urlpatterns = [
    path('user_register', views.UserRegister.as_view(), name='user_register'),
    path('user_login', views.UserLogin.as_view(), name='user_login')
]
