from django.db import models

# Create your models here.
class WebUser(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=10)
