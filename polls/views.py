from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    return HttpResponse(f"You're looking at the question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You are looking at the result of {question_id}")


