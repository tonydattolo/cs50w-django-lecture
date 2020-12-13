from re import search
from django.urls import path

from . import views
from .views import WikiListView, WikiDetailView, WikiCreateView, WikiUpdateView, WikiDeleteView

app_name = "wiki"
urlpatterns = [
    # ex: /wiki/
    path('', WikiListView.as_view(), name="wiki-list"),
    path('wiki/<str:wikiEntry>/', WikiDetailView.as_view(), name="wiki-detail"),
    path('wiki/<str:wikiEntry>/update', WikiUpdateView.as_view(), name="wiki-update"),
    path('wiki/<str:wikiEntry>/delete', WikiDeleteView.as_view(), name="wiki-delete"),
    path('wiki/create', WikiCreateView.as_view(), name="wiki-create")
    # path('wiki/<str:wikiEntry>/update')
    # ex: /wiki/EntryPageName
    # path("wiki/<str:entry>/", views.displayEntry, name="displayEntry"),
    # path("wiki/search/", views.searchView, name="searchView")
    # path("wiki/search/", SearchView.as_view(), name="searchView")
]
