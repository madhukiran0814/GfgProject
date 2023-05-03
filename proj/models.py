from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField('Work')

class Work(models.Model):
    WORK_TYPE_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    )
    link = models.URLField(max_length=255)
    work_type = models.CharField(max_length=255, choices=WORK_TYPE_CHOICES)
