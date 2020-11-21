from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def tony(request):
    return HttpResponse("Hello, Tony!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    }) #optional third argument called the context, all info to provide to the template, variables ie
