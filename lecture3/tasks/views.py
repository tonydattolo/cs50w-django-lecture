from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# tasks = ["foo","bar","baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):

    # store tasks inside the users session, so other sessions cant see. sessions determined by cookies
    # check if there are already tasks stored in the session
    if "tasks" not in request.session:
        request.session["tasks"] = []
        #need py manage.py migrate in order to create default tables inside of djangos database
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] #pass in the list of session tasks to the tasks variable to use in the template
        # django template : python variable
    })

def addTask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST) # contains all of the data that the user submitted when they submitted the form
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            
            return HttpResponseRedirect(reverse("tasks:index")) #figure out what the url of the index url for the tasks app is, and use that
        else:
            return render(request, "tasks/addTask.html", {
                "form": form # send back what they submitted so they can see whats wrong
            })
    return render(request,"tasks/addTask.html", {
        "form": NewTaskForm() 
    })
