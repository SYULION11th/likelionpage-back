# Generated by Django 4.1.5 on 2023-02-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SYUpage', '0008_alter_jungbo_department_alter_jungbo_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jungbo',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
