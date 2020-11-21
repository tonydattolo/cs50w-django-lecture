# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tony", views.tony, name="tony"),
    path("<str:name>", views.greet, name="greet")
]