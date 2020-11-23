from django.urls import path

from . import views


# app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("createNewPage", views.createNewPage, name="createNewPage"),
    path("<str:entryName>", views.displayEntryPage, name="displayEntryName")
]
