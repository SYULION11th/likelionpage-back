# Generated by Django 4.1.5 on 2023-02-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SYUpage', '0003_jungbo_cooperation_jungbo_spend_time_jungbo_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jungbo',
            name='cooperation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jungbo',
            name='spend_time',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jungbo',
            name='track',
            field=models.TextField(),
        ),
    ]
