from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from . models import Question, Choice
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list' : latest_question_list
  }
  return HttpResponse(template.render(context, request))
  
  return HttpResponse(output)
  
def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question':question})
  
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)           
    try:
        next_ques_id = int(question_id) + 1
        next_question = get_object_or_404(Question, pk=next_ques_id)
        return render(request, 'polls/results.html', {'question': question, 'next_question':next_question})
    except:
        return render(request, 'polls/results.html', {'question': question})
        
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print(selected_choice.votes)
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        
def overall_results(request):
  question = Question.objects.all()
  return render(request, 'polls/overall_results.html', {'question' : question})