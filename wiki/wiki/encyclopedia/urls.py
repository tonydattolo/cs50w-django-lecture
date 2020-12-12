from re import search
from django.urls import path

from . import views
from .views import WikiListView, WikiDetailView

app_name = "wiki"
urlpatterns = [
    # ex: /wiki/
    path('', WikiListView.as_view(), name="wiki-list"),
    path('wiki/<str:wikiEntry>/', WikiDetailView.as_view(), name="wiki-detail")
    # ex: /wiki/EntryPageName
    # path("wiki/<str:entry>/", views.displayEntry, name="displayEntry"),
    # path("wiki/search/", views.searchView, name="searchView")
    # path("wiki/search/", SearchView.as_view(), name="searchView")
]
