
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('kursy.html', views.kursy, name="kursy"),
]
