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

def RandomPageView(request):
    entryCount = Entry.objects.all().count()
    randomID = rn.randint(0, entryCount)
    randomEntry = Entry.objects.get(pk=randomID)
    print(f"{entryCount=}, {randomID=}, {randomID=}")
    return redirect('wiki:wiki-detail', wikiEntry=randomEntry.title)
    # return HttpResponseRedirect(reverse('wiki:wiki-detail', kwargs={"wikiEntry": randomEntry}))


class WikiCreateView(CreateView):
    template_name = "encyclopedia/wiki_create.html"
    queryset = Entry.objects.all()
    form_class = EntryForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # Customizing GET and POST methods, inherited from View class

    # def get(self, request, id=None, *args, **kwargs):
    #     form = EntryForm()
    #     context = {
    #         "form": form
    #     }
    #     return render(request, self.template_name, context)
    # def post(self, request, *args, **kwargs):
    #     form = EntryForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     context = {
    #         "form": form
    #     }
    #     return render(request, self.template_name, context)


class WikiUpdateView(UpdateView):
    template_name = "encyclopedia/wiki_update.html"
    queryset = Entry.objects.all()
    form_class = EntryForm

    def get_object(self):
        x = self.kwargs.get("wikiEntry")
        return get_object_or_404(Entry, title=x)

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

    # Override Success Redirect:
    # success_url = "whatever"
    # def get_success_url(self) -> str:
    #     return "whatever"

    # populating with existing data?
    # def render_initial_data(self, request, *args, **kwargs):
    #     initial_data = {
    #         "title": "fill",
    #         "content": "fill"
    #     }
    #     obj = Entry.objects.get(title=self.kwargs.get("idk"))
    #     form = EntryForm(request.POST, initial=initial_data, initial=obj)
    #     context = {
    #         "form": form
    #     }
    #     return render(request, self.template_name, context)

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
    # paginate_by = 25
    context_object_name = "searchResults"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search = self.request.GET.get('q')
    #     query = queryset.filter(title__iexact=search)
    #     print(f"{search=}, {query=}, {query.first().title}")
    #     # if query.exists():
    #     #     return redirect('wiki:wiki-detail', kwargs={"wikiEntry":str(query.first().title)} )
    #     # return queryset.filter(Q(title__icontains=search))
    #     object_list = Entry.objects.filter(Q(title__icontains=search))
    #     print(f"{self.queryset=}")
    #     return object_list

    def get_queryset(self):
        search = self.request.GET.get('q')
        # test = Entry.objects.filter(Q(title__icontains=search))
        try:
            return Entry.objects.filter(Q(title__icontains=search))
        # except Entry.DoesNotExist:
        except:
            return "no such THINGY"

    def get(self, request, *args, **kwargs):
        print(f"{self.request.GET.get('q')=}")
        print(f"{self.get_queryset().first().title=}")
        print(f"{len(self.get_queryset())=}")
        if len(self.get_queryset()) == 1:
            if self.request.GET.get('q') == self.get_queryset().first().title:
                return redirect('wiki:wiki-detail', wikiEntry=self.get_queryset().first().title)

        context = {"searchResults": self.get_queryset()}
        return render(request, self.template_name, context)

    # def get_queryset(self):
    #     search = self.request.GET.get('q')
    #     try:
    #         testerino = Entry.objects.get(title=search)
    #         return redirect(testerino)
    #     except:
    #         object_list = Entry.objects.filter(Q(title__icontains=search))
    #     return object_list



    # stackoverflow try
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     q = self.request.GET.get("q")
    #     if q:
    #         queryset = queryset.filter(title__icontains=q)
    #         # try:
    #         #     queryset = queryset.get(title=)
    #         # except expression as identifier:
    #         #     pass
    #     return queryset
# ##############################################################

# class NewEntryForm(forms.Form):
#     entryTitle = forms.CharField(label="New Entry Title")
#     # entryContent = forms.CharField(
#     #     label="Entry Content in Markdown",
#     #     widget=forms.Textarea(attrs={"rows":3, "cols":5}))
#     entryContent = forms.Textarea()

# class SearchForm(forms.Form):
#     q = forms.CharField(label="search", max_length=64)

# class IndexPageView(ListView):
#     template_name = "index.html"
#     # form_class = SearchForm
#     model = Entry


# def index(request):
#     return render(request, "encyclopedia/index.html", {
#         "allEntries": Entry.objects.all(),
#         "searchbox": SearchForm()
#     })

# def displayEntry(request, entry):
#     try:
#         entryData = Entry.objects.get(title=entry)
#         entryTitle = entryData.title
#         entryHTML = markdown2.markdown(entryData.content)
#         return render(request, "encyclopedia/displayEntry.html", {
#             "entryTitle": entryTitle,
#             "entryHTML": entryHTML
#         })
#     except:
#         return render(request, "encyclopedia/displayEntry.html")

# class EntryListView(ListView):
#     model = Entry
#     paginate_by = 100
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         q = self.request.GET.get("q")
#         if q:
#             queryset = queryset.filter(title__icontains=q)
#         return queryset

# class EntryDetailView(DetailView):
#     model = Entry

# def searchView(request):
#     searchedTerm = request.GET.get('q')
#     try:
#         exactMatch = Entry.objects.get(title=searchedTerm)
#         entryTitle = exactMatch.title
#         entryHTML = markdown2.markdown(exactMatch.content)
#         return render(request, "encyclopedia/displayEntry.html", {
#             "entryTitle": entryTitle,
#             "entryHTML": entryHTML
#         })
#     except:
#         try:
#             searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
#             return render(request, "encyclopedia/searchResults.html", {
#                 "searchResults": searchResults,
#                 "searchedTerm": searchedTerm
#             })
#         except:
#             return render(request, "encyclopedia/searchResults.html", {
#             "emptyResults": f"No entries found matching: {searchedTerm}",
#             "searchedTerm": searchedTerm
#         })

# class SearchView(ListView):
#     template_name = "encyclopedia/searchResults.html"
#     model = Entry
#     context_object_name = "searchList"

#     def get_queryset(self):
#         searchedTerm = self.request.GET.get('q')
#         try:
#             searchResults = Entry.objects.get(title=searchedTerm)
#             return searchResults
#         except:
#             try:
#                 searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
#                 return searchResults
#             except:
#                 pass
            
#     def as_view():
#         searchedTerm = self.request.GET.get('q')
#         try:
#             exactMatch = Entry.objects.get(title=searchedTerm)
#             entryTitle = exactMatch.title
#             entryHTML = markdown2.markdown(exactMatch.content)
#             return render(request, "encyclopedia/displayEntry.html", {
#                 "entryTitle": entryTitle,
#                 "entryHTML": entryHTML,
#             })
#         except:
#             searchResults = Entry.objects.filter(Q(title__icontains=searchedTerm))
#             return render(request, "encyclopedia/searchResults.html", {
#                 "searchResults": searchResults,
#                 "searchedTerm": searchedTerm
#             })
#         else:
#             return render(request, "encyclopedia/searchResults.html", {
#                 "emptyResults": f"No entries found matching: {searchedTerm}",
#                 "searchedTerm": searchedTerm
#             })
        
        
            
        