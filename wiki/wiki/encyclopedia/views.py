import re
from django.db.models import query
from django.db.models.query_utils import Q
from django.http import request
from django.shortcuts import render
from django import forms
from django.views.generic import ListView, FormView
from django.views.generic.base import View

from . import util
from .models import Entry

import markdown2


# can separate forms into forms.py and just import them, same as models
class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="New Entry Title")
    # entryContent = forms.CharField(
    #     label="Entry Content in Markdown",
    #     widget=forms.Textarea(attrs={"rows":3, "cols":5}))
    entryContent = forms.Textarea()

class SearchForm(forms.Form):
    q = forms.CharField(label="search", max_length=64)

class IndexPageView(View):
    template_name = "index.html"
    # form_class = SearchForm

    def as_view(self, request):
        return render(request, "encyclopedia/index.html", {
        "allEntries": Entry.objects.all(),
        "searchbox": SearchForm()
    })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "allEntries": Entry.objects.all(),
        "searchbox": SearchForm()
    })

def displayEntry(request, entry):
    try:
        entryData = Entry.objects.get(title=entry)
        entryTitle = entryData.title
        entryHTML = markdown2.markdown(entryData.content)
        return render(request, "encyclopedia/displayEntry.html", {
            "entryTitle": entryTitle,
            "entryHTML": entryHTML
        })
    except:
        return render(request, "encyclopedia/displayEntry.html")

def searchView(request):
    searchedTerm = request.GET.get('q')
    try:
        exactMatch = Entry.objects.get(title=searchedTerm)
        entryTitle = exactMatch.title
        entryHTML = markdown2.markdown(exactMatch.content)
        return render(request, "encyclopedia/displayEntry.html", {
            "entryTitle": entryTitle,
            "entryHTML": entryHTML
        })
    except:
        try:
            searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
            return render(request, "encyclopedia/searchResults.html", {
                "searchResults": searchResults,
                "searchedTerm": searchedTerm
            })
        except:
            return render(request, "encyclopedia/searchResults.html", {
            "emptyResults": f"No entries found matching: {searchedTerm}",
            "searchedTerm": searchedTerm
        })

class SearchView(ListView):
    template_name = "encyclopedia/searchResults.html"
    model = Entry
    context_object_name = "searchList"

    def get_queryset(self):
        searchedTerm = self.request.GET.get('q')
        try:
            searchResults = Entry.objects.get(title=searchedTerm)
            return searchResults
        except:
            try:
                searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
                return searchResults
            except:
                pass
            
    def as_view():
        searchedTerm = self.request.GET.get('q')
        try:
            exactMatch = Entry.objects.get(title=searchedTerm)
            entryTitle = exactMatch.title
            entryHTML = markdown2.markdown(exactMatch.content)
            return render(request, "encyclopedia/displayEntry.html", {
                "entryTitle": entryTitle,
                "entryHTML": entryHTML,
            })
        except:
            searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
            return render(request, "encyclopedia/searchResults.html", {
                "searchResults": searchResults,
                "searchedTerm": searchedTerm
            })
        else:
            return render(request, "encyclopedia/searchResults.html", {
                "emptyResults": f"No entries found matching: {searchedTerm}",
                "searchedTerm": searchedTerm
            })
        
        
            
        