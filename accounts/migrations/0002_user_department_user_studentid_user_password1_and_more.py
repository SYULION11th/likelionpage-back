# Generated by Django 4.1.5 on 2023-01-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Department',
            field=models.CharField(default='Department', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='StudentID',
            field=models.CharField(default='StudentID', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default='password1', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='password2', max_length=30),
        ),
    ]
