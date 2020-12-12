from django.urls import path
from .views import (
    # views
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="article-list"),
    path('<int:id>', ArticleDetailView.as_view(), name="article-detail"), #can customize lookup
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="article-delete")
]
# class based views look for a specific template
# <app name>/<model name>_<generic view name>.html
# blog/modelname_list.html