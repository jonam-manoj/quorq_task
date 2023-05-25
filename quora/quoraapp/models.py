

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)