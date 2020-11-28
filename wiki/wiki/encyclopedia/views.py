import re
from django.shortcuts import render
from django import forms

from . import util
from .models import Entry

import markdown2

class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="New Entry Title")
    # entryContent = forms.CharField(
    #     label="Entry Content in Markdown",
    #     widget=forms.Textarea(attrs={"rows":3, "cols":5}))
    entryContent = forms.Textarea()

class SearchForm(forms.Form):
    term = forms.CharField(max_length=50)

def index(request):
    return render(request, "encyclopedia/index.html", {
        # "entries": util.list_entries(),
        "allEntries": Entry.objects.all(),
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

def search(request, q):
    try:
        exactMatch = Entry.objects.get(title=q)
        displayEntry(request, exactMatch)
    except:
        return render(request, "encyclopedia/searchResults.html", {
            "searchResults": Entry.objects.filter(title__icontains=q),
            "searchedTerm": q
        })
    else:
        pass

