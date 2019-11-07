from django.db import models

# manage.py makemigrations polls
# Create your models here.
class WebUser(models.Model):
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    pw = models.CharField(max_length=10)
    birth = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    subject = models.CharField(max_length=1)

class Book(models.Model):
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    subject = models.CharField(max_length=1)