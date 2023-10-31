from django.contrib import admin
from django.urls import path,include
from quiz import views
from . import views



urlpatterns =[
        path("",views.home,name = "dashboard"),
        path('teacher_login',views.teacher_login,name = "teacher_login"),
        path('teacher_registration',views.teacher_registration,name = "teacher_registration"),
        path('teacher_login',views.teacher,name = "teacher"),
        path('student', views.quiz_home, name='quiz_home'),
        path('<int:subject_id>/', views.quiz_detail, name='quiz_detail'),
        path('<int:subject_id>/submit/', views.submit_quiz, name='submit_quiz'),
        path('add_questions', views.add_questions, name='add_questions'),
        path('add_subjects', views.add_subjects, name='add_subjects'),
        path('add_choices', views.add_choices, name='add_choices'),
        
        
        
        
        
        
]
