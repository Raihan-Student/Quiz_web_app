# Generated by Django 4.2.6 on 2023-10-30 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizresult',
            name='total_marks',
        ),
        migrations.RemoveField(
            model_name='quizresult',
            name='total_questions',
        ),
    ]
