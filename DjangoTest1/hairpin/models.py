from django.db import models

class hairpin(models.Model):
    name = models.CharField(max_length=200, default="x")
    color = models.CharField(max_length=200, default="x")
    url = models.URLField(max_length=200, default="x")

class post(models.Model):
    author = models.CharField(max_length=200, default="x")
    title = models.CharField(max_length=200, default="x")
    mood = models.CharField(max_length=200, default="x")





