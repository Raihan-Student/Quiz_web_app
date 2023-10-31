
from multiprocessing import AuthenticationError
from telnetlib import AUTHENTICATION
from quiz import admin
from quiz.forms import ChoiceForm, QuestionForm, SubjectForm
from quizapps import settings
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail


from django.http import HttpResponse
from django.template.loader import get_template
#this import functions is for  quiz section
from django.shortcuts import render, get_object_or_404
from .models import Subject, Question, Choice, QuizResult
#this library is used for Questions  uploading by teachers
def add_subjects(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'teacher.html')
    else:
        form = SubjectForm()
    return render(request, 'add_subjects.html', {'form': form})

def add_questions(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'teacher.html')
    else:
        form = QuestionForm()
    return render(request, 'add_questions.html', {'form': form})
def add_choices(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'teacher.html')
    else:
        form = ChoiceForm()
    return render(request, 'add_choices.html', {'form': form})




#this sections is for quiz
def quiz_home(request):
    subjects = Subject.objects.all()
    return render(request, 'quiz_home.html', {'subjects': subjects})

def quiz_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    questions = Question.objects.filter(subject=subject)
    return render(request, 'quiz_detail.html', {'subject': subject, 'questions': questions})

def submit_quiz(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    questions = Question.objects.filter(subject=subject)
    score = 0
    for question in questions:
        selected_choice = request.POST.get(f'question_{question.id}')
        if selected_choice:
            choice = question.choice_set.get(pk=selected_choice)
            if choice.is_correct:
                score += 1
    quiz_result = QuizResult(user_name="Test User", subject=subject, score=score)
    quiz_result.save()
    return render(request, 'result.html', {'subject': subject, 'score': score})




























def home(request):
    return render(request,'home.html')
def teacher_login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'teacher.html')
        else:
            messages.error(request,"invalid username or password")
            return redirect('teacher_login')
    return render(request,'teacher_login.html')

def teacher_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username):
            #messages.error(request,"username already exists")
            return redirect('teacher_registration')
            
        if User.objects.filter(email=email):
            #messages.error(request,"email already exists")
            return redirect('teacher_registration')
        if len(username)>15:
            #messages.error(request,"username must be less than 15 characters")
            
            return redirect('teacher_registration')
        if password1!=password2:
            #messages.error(request,"password did not match")
            return redirect('teacher_registration')
        teacher = User.objects.create_user(username,email,password1)
        teacher.save()
       
         
        
        return redirect('teacher_login')
    return render(request,'teacher_registration.html')
def teacher(request):
    return render(request,'teacher.html')
    
#for Student

def student(request):
    return render(request,'student.html')

#def dbms(request):
    return render(request,'dbms.html')
#def network(request):
    return render(request,'networks.html')
#def machine(request):
    return render(request,'ml.html')
#def python(request):
    return render(request,'python.html')
#def dsa(request):
    return render(request,'dsa.html')
#def iot(request):
    return render(request,'iot.html')

#def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username):
            #messages.error(request,"username already exists")
            return redirect('signup')
            
        if User.objects.filter(email=email):
            #messages.error(request,"email already exists")
            return redirect('signup')
        if len(username)>15:
            #messages.error(request,"username must be less than 15 characters")
            
            return redirect('signup')
        if password1!=password2:
            #messages.error(request,"password did not match")
            return redirect('signup')
        myuser = User.objects.create_user(username,email,password1)
        myuser.save()
       
           # for email verification 
        #messages.success(request,"Your account has been created successfully")
        #subject = "welcome to our website"
        #messages = "Hello"+myuser.username+"!! \n"+"welcome  to our website \n we have sent you an email please verify your account"
        #from_email = settings.EMAIL_HOST_USER
        #to_list = [myuser.email]
       # send_mail(subject,messages,from_email, to_list,fail_silently=True)
        
        return redirect('student_login')
        
    return render(request,"signup.html")
#def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password1=password)
        if user is AUTHENTICATION:
            login(request,user)
           
            return render(request,'home.html')
        else:
            #pass
           return render(request,'login.html')
    
    return render(request,"login.html")