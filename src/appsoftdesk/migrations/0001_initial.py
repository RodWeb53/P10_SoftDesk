# Generated by Django 4.2.1 on 2023-06-18 05:48

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
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('back-end', 'Be'), ('Front-end', 'Fe'), ('IOS', 'Ios'), ('Android', 'An')], max_length=70)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('desc', models.CharField(max_length=255)),
                ('tag', models.CharField(choices=[('Bug', 'Bu'), ('Improvement', 'Im'), ('Task', 'Ta')], max_length=70)),
                ('priority', models.CharField(choices=[('Low', 'L'), ('Medium', 'M'), ('High', 'H')], max_length=70)),
                ('status', models.CharField(choices=[('To Do', 'Td'), ('In progress', 'Ip'), ('Donne', 'Do')], max_length=70)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue_assignee', to=settings.AUTH_USER_MODEL)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue_author', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issues_project', to='appsoftdesk.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments_issue', to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments_issue', to='appsoftdesk.issues')),
            ],
        ),
        migrations.CreateModel(
            name='Contributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('Creator', 'Creator'), ('Contributor', 'Contrib')], max_length=70)),
                ('role', models.CharField(max_length=255)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsoftdesk.projects')),
            ],
            options={
                'unique_together': {('author_user', 'project')},
            },
        ),
    ]
