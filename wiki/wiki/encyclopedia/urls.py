from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    # ex: /encyclopedia/
    path("", views.index, name="index"),
    # ex: /encyclopedia/EntryPageName
    path("wiki/<str:entry>/", views.displayEntry, name="displayEntry")
]
