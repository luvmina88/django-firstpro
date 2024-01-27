from django.db import models


class Question(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.DateField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Meta:
    pass
