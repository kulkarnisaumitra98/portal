from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.TextField()
    choice1 = models.CharField(max_length=126)
    choice2 = models.CharField(max_length=126)
    choice3 = models.CharField(max_length=126)
    choice4 = models.CharField(max_length=126)
    correct = models.CharField(max_length=1)

    def __str__(self):
        return self.questions


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    nofquestion = models.IntegerField(default=0)
    lastQuestion = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.user.username