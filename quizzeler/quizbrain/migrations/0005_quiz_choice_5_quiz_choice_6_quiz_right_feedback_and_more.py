# Generated by Django 4.0.3 on 2022-04-16 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizbrain', '0004_rename_choice_list_quiz_choice_1_quiz_choice_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='choice_5',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='choice_6',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='right_feedback',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='wrong_feedback',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
