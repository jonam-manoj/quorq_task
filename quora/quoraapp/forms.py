from django import forms
from .models import Question, Answer
from quoraapp.models import UserProfileInfo
from django.contrib.auth.models import User
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','email','password']