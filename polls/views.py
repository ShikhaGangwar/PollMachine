from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    latest_question_list =Question.objects.order_by('-pub_date')[:3]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/index.html', {'questions': question})

def results(request, question_id):
    return HttpResponse("You are looking at the results of %s "%question_id)