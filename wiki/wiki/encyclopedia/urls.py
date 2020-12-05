from re import search
from django.urls import path

from . import views
from .views import IndexPageView, SearchView

app_name = "wiki"
urlpatterns = [
    # ex: /wiki/
    path("", views.index, name="index"),
    # path("", IndexPageView.as_view(), name="index"),
    # ex: /wiki/EntryPageName
    path("wiki/<str:entry>/", views.displayEntry, name="displayEntry"),
    # path("wiki/search/", views.searchView, name="searchView")
    path("wiki/search/", SearchView.as_view(), name="searchView")
]
