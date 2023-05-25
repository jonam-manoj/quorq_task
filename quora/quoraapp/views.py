

# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from quoraapp.forms import UserForm

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'post_qution.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = AnswerForm()
    return render(request, 'answer_qution.html', {'form': form, 'question': question})


# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('quoraapp:home'))

            else:
                return HttpResponse("Account is not active")

        else:
            print("login failed!! please try again after sometime")
            return HttpResponse("Invalid login credentials")

    else:
        return render(request,'login.html',{})

# def user_register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

def user_register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # set_password method converts password into hashing password
            user.save()


            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()


    return render(request,'register.html',{'user_form':user_form,
                                                        "registered":registered})



