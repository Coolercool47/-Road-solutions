from django.db import models


class Feedback(models.Model):
    problem_name = models.CharField(max_length=50)
    problem_text = models.TextField(max_length=1500)
    address = models.CharField(max_length=50)
    date = models.DateField()
