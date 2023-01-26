from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BookAPI.as_view(), name='book')
]