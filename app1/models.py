from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


# class blog(models.Model):
#     title = models.CharField(max_length=40)
#     description = models.TextField(max_length=7000)


class post(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=7000)
    posted_date = models.DateField(default=timezone.now)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_posts')
