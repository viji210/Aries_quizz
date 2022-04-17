from django.db import models

# Create your models here.


class Quiz(models.Model):
    category = models.CharField(max_length=250)
    question = models.CharField(max_length=1000)
    code_in_question = models.CharField(max_length=800, blank=True, null=True)
    choice_1 = models.CharField(max_length=1000)
    choice_2 = models.CharField(max_length=1000)
    choice_3 = models.CharField(max_length=1000)
    choice_4 = models.CharField(max_length=1000, blank=True, null=True)
    choice_5 = models.CharField(max_length=1000, blank=True, null=True)
    choice_6 = models.CharField(max_length=1000, blank=True, null=True)
    right_feedback = models.CharField(max_length=1000)
    wrong_feedback = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.category}; {self.question}"
