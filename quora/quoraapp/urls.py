from django.urls import path
from quoraapp import views 
#from .views import user_login

app_name = 'quoraapp'

urlpatterns = [
    path('',views.home,name="home"),
    path('post_question/',views.post_question,name="post_question"),
    path('answer_question/',views.answer_question,name="answer_question"),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),

]