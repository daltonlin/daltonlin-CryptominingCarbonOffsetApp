from django.db import models
from django.contrib.auth.models import User


class Start(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#user's identifier, user's data will be deleted only after the user is deleted
    user_name = models.CharField(max_length=100)#project's name
    time_started = models.DateTimeField(auto_now_add=True) #auto_now_add=True to ensure that the start time data is unable to be modified

class



