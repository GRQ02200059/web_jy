from __future__ import unicode_literals
from django.db import models
class Actions(models.Model):
    date=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
class Links(models.Model):
    book=models.CharField(max_length=100)
    person_a=models.CharField(max_length=100)
    a_id=models.CharField(max_length=100)
    person_b=models.CharField(max_length=100)
    b_id=models.CharField(max_length=100)
    relation=models.CharField(max_length=100)
class Persons(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    book=models.CharField(max_length=100)

