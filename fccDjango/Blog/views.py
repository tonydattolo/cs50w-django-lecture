from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)

from .models import Article
from .forms import ArticleForm, RawArticleForm
# Create your views here.

class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = "Blog/article_list.html"

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    queryset = Article.objects.all()
    template_name = "Blog/article_create.html"

    def form_valid(self, form):
        print(form.cleaned_data())
        return super().form_valid(form)

    # change where you want it to go
    # option 1: set var
    success_url = '/'
    # option 2: def the var
    # def get_success_url(self) -> str:
    #     return '/'

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    queryset = Article.objects.all()
    template_name = "Blog/article_update.html"

    def form_valid(self, form):
        print(form.cleaned_data())
        return super().form_valid(form)

    # same as create except here we're grabbing an instance of the object to change it
    def get_object(self):
        id_ = self.kwargs.get("id") #takes in given kwarg from the url regex, can customize
        return get_object_or_404(Article, id=id_)


# the primary function of a detail view, is to render a template from a specific object
class ArticleDetailView(DetailView):
    # queryset limits choices available for that detailview
    queryset = Article.objects.all()
    template_name = "Blog/article_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id") #takes in given kwarg from the url regex, can customize
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    # queryset limits choices available for that detailview
    queryset = Article.objects.all()
    template_name = "Blog/article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id") #takes in given kwarg from the url regex, can customize
        return get_object_or_404(Article, id=id_)

def article_create_view(request):
    form = RawArticleForm() #initialize form, render for get
    
    # check if method is post
    if request.method == "POST":
        # take in the data the user submitted and save it as a form
        form = RawArticleForm(request.POST) #render for post request
        # check if form data is valid server-side
        if form.is_valid():
            # create new DB object from form. ** turns it into args to pass
            Article.objects.create(**form.cleaned_data)
        else:
            return render(request, 'Blog/article_create.html', {
                "createArticleForm": form
            })

    context = {
        "createArticleForm": form
    }
    return render(request, 'Blog/article_create.html', context)

def article_create_view2(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        "createArticleForm": form
    }
    return render(request, 'Blog/article_create.html', context)