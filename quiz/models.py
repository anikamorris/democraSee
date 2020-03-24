from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    AGREE = 'agree'
    DISAGREE = 'disagree'
    options = [
        (AGREE,'agree'),
        (DISAGREE, 'disagree')
    ]
    q_choices = models.CharField(max_length=8,choices=options)
    what = models.TextChoices('Agree', 'Disagree')
    def __str__(self):
        return self.q_choices
    

