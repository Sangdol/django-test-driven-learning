from django.http import HttpResponse

from .models import Question


# Each view either returns an HttpResponse or raises an exception such as Http404.
def index(request):
    # What does the preceding dash mean?
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = "<br>".join([q.question_text for q in latest_question_list])

    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at question $s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
