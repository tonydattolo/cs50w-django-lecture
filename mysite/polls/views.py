from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latestQuestionList"

    def get_queryset(self):
        """return the last 5 published questions"""
        return Question.objects.order_by('-pubDate')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# Create your views here.
def index(request):
    latestQuestions = Question.objects.order_by("-pubDate")[:5]
    return render(request, "polls/index.html", {
        "latestQuestions": latestQuestions
    })

def detail(request, question_id):
    # Shortened version
    question = get_object_or_404(Question, pk=question_id)
    # syntax     get_object_or_404(Model, model attribute kwargs to check if wanted object exists) uses .get()
    #            get_list_of_404() same but uses .filter and returns list
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {
        'question': question
    })

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        "question": question
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form 
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POSTdara. This prevents data from being posted twice if a 
        # user hits the back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id)))