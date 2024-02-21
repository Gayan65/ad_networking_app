from django.urls import path
from . import views

urlpatterns = [
    path('sun_app/', views.sun_app, name='sun_app'),
    path('', views.bun_app, name='bun_app'),
]
