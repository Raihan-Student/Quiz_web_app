# Generated by Django 4.2.6 on 2023-10-31 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_choice_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='subject',
        ),
    ]
