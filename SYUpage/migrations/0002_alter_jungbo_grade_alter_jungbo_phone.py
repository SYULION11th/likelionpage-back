# Generated by Django 4.1.5 on 2023-02-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SYUpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jungbo',
            name='grade',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='jungbo',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
