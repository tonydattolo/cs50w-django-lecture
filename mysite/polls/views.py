from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Choice, Question

# Create your views here.
def index(request):
    latestQuestions = Question.objects.order_by("-pubDate")[:5]
    return render(request, "polls/index.html", {
        "latestQuestions": latestQuestions
    })

def detail(request, question_id):
    # Shortened version
    # question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {
        'question': question
    })

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")


