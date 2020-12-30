from django.urls import path

from .views import (
    randomPageView, WikiListView,
    WikiDetailView,
    WikiCreateView,
    WikiUpdateView,
    WikiDeleteView,
    WikiSearchView
)

app_name = "wiki"
urlpatterns = [
    # ex: /wiki/
    path('', WikiListView.as_view(), name="wiki-list"),
    path('wiki/<str:wikiEntry>/', WikiDetailView.as_view(), name="wiki-detail"),
    path('wiki/<str:wikiEntry>/update', WikiUpdateView.as_view(), name="wiki-update"),
    path('wiki/<str:wikiEntry>/delete', WikiDeleteView.as_view(), name="wiki-delete"),
    path('wiki/create', WikiCreateView.as_view(), name="wiki-create"),
    path('wiki/search_results', WikiSearchView.as_view(), name="wiki-search"),
    path('random/', randomPageView, name="wiki-random" )
    # path('wiki/<str:wikiEntry>/update')
    # ex: /wiki/EntryPageName
]
