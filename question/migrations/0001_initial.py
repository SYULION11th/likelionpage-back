# Generated by Django 4.1.5 on 2023-01-30 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('qtitle', models.CharField(max_length=50)),
                ('quest_text', models.TextField()),
                ('qimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('qcreated_at', models.DateTimeField(auto_now_add=True)),
                ('qupdated_at', models.DateTimeField(auto_now_add=True)),
                ('quser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=500)),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qcomments', to='question.quest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
