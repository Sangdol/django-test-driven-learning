from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


# Each view either returns an HttpResponse or raises an exception such as Http404.
def index(request):
    # What does the preceding dash mean?
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


def detail_old(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


# There's also `get_list_or_404()`
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
