from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dynamic/", views.weatherAPI, name="weatherAPI"),
    path("forms/", views.forms, name="forms"),
]
