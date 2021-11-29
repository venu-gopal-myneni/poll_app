from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question
# Create your views here.


def welcome(request):
    return HttpResponse("Hello !! Welcome to the First View of the polls sub-app")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)
    # return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


'''
def get_questions(request):
    question_list = Question.objects.order_by("pub_date")
    # print(question_list)
    template = loader.get_template("polls/get_questions.html")
    q_string = ",".join([Q.question_text for Q in question_list])
    # return HttpResponse(f"No of questions = {len(question_list)}\n"f"{q_string}")
    context = {"latest_question_list": question_list}
    return HttpResponse(template.render(context, request))
'''


def get_questions(request):
    question_list = Question.objects.order_by("pub_date")
    # print(question_list)
    template = loader.get_template("polls/get_questions.html")
    q_string = ",".join([Q.question_text for Q in question_list])
    # return HttpResponse(f"No of questions = {len(question_list)}\n"f"{q_string}")
    context = {"latest_question_list": question_list}
    return render(request, "polls/get_questions.html", context)
