from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Question
from django.template import loader

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    #context = {
    #    'latest_question_list': latest_question_list,
    #}
    #return HttpResponse(template.render(context, request))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("将为您打开问卷 %s。" % question_id)

def results(request, question_id):
    response = "正在查看问卷%s的结果。"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("请为问卷%s提交您的答案。" % question_id) 
