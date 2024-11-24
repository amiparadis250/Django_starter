from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello_world'),
    path('login/', views.Login, name='hello_world'),
]
