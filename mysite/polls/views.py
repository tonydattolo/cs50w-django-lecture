from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Choice, Question

# Create your views here.
def index(request):
    latestQuestions = Question.objects.order_by("-pubDate")[:5]
    return render(request, "polls/index.html", {
        "latestQuestions": latestQuestions
    })

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")


