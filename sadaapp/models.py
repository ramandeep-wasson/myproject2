from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()

