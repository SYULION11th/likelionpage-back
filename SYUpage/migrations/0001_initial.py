# Generated by Django 4.1.5 on 2023-01-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JungBo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Department', models.CharField(default='Department', max_length=30)),
                ('studentid', models.IntegerField()),
                ('grade', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
