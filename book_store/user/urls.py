from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('show', views.show, name='show'),
    path('login', views.login, name='login')
]
