# Generated by Django 4.2.6 on 2023-10-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_remove_choice_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]
