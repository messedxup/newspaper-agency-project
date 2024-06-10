from django.shortcuts import render

from newspaper.models import Redactor, Topic, Newspaper


def index(request):
    redactors = Redactor.objects.all()
    topics = Topic.objects.all()
    newspapers = Newspaper.objects.all()
    context = {
        "redactors": redactors,
        "newspapers": newspapers,
        "topics": topics
    }
    return render(request, "newspaper/index.html", context=context)
