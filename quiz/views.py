from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from quiz.models import Question
from .models import Choice
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .forms import SecondQuizForm




def display(request):
    
    context_object_name = 'latest_question_list'
    questions = Question.objects.all()
       # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SecondQuizForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('quiz:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SecondQuizForm()
    return render(request, 'quiz/questions.html', {
            'form': form, 'questions':questions})


def vote(request):
    question = get_object_or_404(Question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'quiz/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz:results'))

class IndexView(generic.ListView):
    model = Question
    template_name = 'quiz/quiz.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        questions = Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        return questions
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'
    def get_queryset(self):
        
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'