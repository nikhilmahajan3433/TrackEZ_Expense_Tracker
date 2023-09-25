from django.db import models

class exp_add(models.Model):
    name=models.CharField(max_length=40)
    value=models.IntegerField()
