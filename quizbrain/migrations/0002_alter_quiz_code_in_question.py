# Generated by Django 4.0.3 on 2022-04-09 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizbrain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='code_in_question',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
