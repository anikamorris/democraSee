from django.forms import ModelForm
from django import forms
from quiz.models import *
from .models import Choice
from django.forms import CheckboxSelectMultiple


class QuizForm(forms.ChoiceField):
      def __init__(self, *args, **kwargs):
            super(QuizForm, self).__init__(*args, **kwargs)
            self.error_messages = {"required":"Please select a response, it's required"}
            self.choices = ((None,'Select a response'),('Agree','Agree'),('Disagree','Disagree'))
        
class SecondQuizForm(forms.Form):
    Model = Question
    options = [
    ('Agree', 'Agree'),
    ('Disagree', 'Disagree')
    ]
    response = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=options,
    )
    
    def quiz_forms(self,data=None):
        questions = Question.objects.all()
        form_list = []
        for i in questions:
            form_list.append(questions)
        return form_list
        print(form_list)


