from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('thanks', views.thanks),
    path('register', views.index),
    path('login', views.login),
    path('logout', views.logout)
]