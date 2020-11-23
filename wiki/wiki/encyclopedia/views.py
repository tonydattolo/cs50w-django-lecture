import re
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls.base import reverse

import markdown2

from . import util

class NewEntryForm(forms.Form):
    entryTitle = forms.CharField(label="New Entry Title")
    entryContent = forms.CharField(
        label="Entry Content in Markdown",
        widget=forms.Textarea(attrs={"rows":3, "cols":5}))
    # dateLastEdited = forms.DateField()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def createNewPage(request):
    # Check if method is POST, or submitting vs viewing new form
    if request.method =="POST":
        # Take in data the user submitted and save it as form
        newEntry = NewEntryForm(request.POST)
        # Check if form data is valid (server-side)
        if newEntry.is_valid():
            # Add new markdown file thus updating list of entries
            util.save_entry(
                newEntry.cleaned_data["entryTitle"],
                newEntry.cleaned_data["entryContent"])
            return HttpResponseRedirect(reverse("encyclopedia:createNewPage"))
        
        # Else, if form has invalid data, re-render with warnings
        else:
            return render(request, "encyclopedia/entryPage.html", {
                "newEntryForm": newEntry
            })
    return render(request, "encyclopedia/entryPage.html", {
        "newEntryForm": NewEntryForm()
    })

def displayEntryPage(request, entryName):
    # names = util.list_entries()
    entryHTML = markdown2.markdown(util.get_entry(entryName))
    return render(request, "encyclopedia/displayEntry.html", {
        "entryName": entryHTML
    })