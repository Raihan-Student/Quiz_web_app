from random import choice
from django import forms

from quiz.models import Choice, Question, QuizResult, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
class QuizResultForm(forms.ModelForm):
    class Meta:
        model = QuizResult
        fields = '__all__'