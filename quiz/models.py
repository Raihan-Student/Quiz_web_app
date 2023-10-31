from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.question_text



class Choice(models.Model):
    
    #subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    choice_text = models.CharField(max_length=200)
    
    is_correct = models.BooleanField(default=False)

class QuizResult(models.Model):
    user_name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()
    #for notes upload by the teacher
