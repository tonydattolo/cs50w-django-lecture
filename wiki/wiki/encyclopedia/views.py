import re
import random as rn
from django.db.models import query
from django.db.models.query_utils import Q
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.views.generic import ListView, FormView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse

from . import util
from .models import Entry
from .forms import EntryForm, SearchForm

import markdown2


# can separate forms into forms.py and just import them, same as models
class WikiListView(ListView):
    queryset = Entry.objects.all()
    template_name = "encyclopedia/index.html"
    context_object_name = "allEntries"
    # form_class = SearchForm
    
    # def get(self, request, *args, **kwargs):
    #     context = {
    #         "allEntries": self.queryset
    #     }
    #     return render(request, self.template_name, context)

# class WikiLayoutView(FormView):
#     template_name = "encyclopedia/layout.html"
#     form_class = SearchForm

class WikiDetailView(DetailView):
    template_name = "encyclopedia/wiki_detail.html"
    queryset = Entry.objects.all()
    context_object_name = "entryTitle"

    # Override default regex arg passed to url to allow for wikiEntry instead of just pk
    def get_object(self):
        x = self.kwargs.get("wikiEntry")
        return get_object_or_404(Entry, title=x)

    def get_context_data(self, *args, **kwargs):
        context = super(WikiDetailView, self).get_context_data(*args,**kwargs)
        # add extra field
        z = Entry.objects.get(title=self.kwargs.get("wikiEntry"))
        context["entryHTML"] = markdown2.markdown(z.content)
        return context

def randomPageView(request):
    entryCount = Entry.objects.all().count()
    randomID = rn.randint(1, entryCount - 1)
    randomEntry = Entry.objects.get(pk=randomID)
    print(f"{entryCount=}, {randomID=}, {randomEntry=}")
    return redirect('wiki:wiki-detail', wikiEntry=randomEntry.title)
    # return HttpResponseRedirect(reverse('wiki:wiki-detail', kwargs={"wikiEntry": randomEntry}))


class WikiCreateView(CreateView):
    template_name = "encyclopedia/wiki_create.html"
    queryset = Entry.objects.all()
    form_class = EntryForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class WikiUpdateView(UpdateView):
    template_name = "encyclopedia/wiki_update.html"
    queryset = Entry.objects.all()
    form_class = EntryForm

    def get_object(self):
        x = self.kwargs.get("wikiEntry")
        return get_object_or_404(Entry, title=x)

class WikiDeleteView(DeleteView):
    template_name = "encyclopedia/wiki_delete.html"

    def get_object(self):
        x = self.kwargs.get("wikiEntry")
        return get_object_or_404(Entry, title=x)
    def get_success_url(self) -> str:
        return reverse('wiki:wiki-list')

class WikiSearchView(ListView):
    template_name = "encyclopedia/wiki_search.html"
    model = Entry
    paginate_by = 25
    context_object_name = "searchResults"

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Entry.objects.filter(Q(title__icontains=search))

    def get(self, request, *args, **kwargs):
        # Check if there is only one entry that matches 
        if len(self.get_queryset()) == 1:
            # Check if it is an exact match, case sensitive
            if self.request.GET.get('q') == self.get_queryset().first().title:
                return redirect('wiki:wiki-detail', wikiEntry=self.get_queryset().first().title)

        context = {"searchResults": self.get_queryset()}
        return render(request, self.template_name, context)


# ##############################################################