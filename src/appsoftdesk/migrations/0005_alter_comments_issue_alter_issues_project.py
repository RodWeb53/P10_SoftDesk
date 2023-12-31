# Generated by Django 4.2.1 on 2023-07-16 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsoftdesk', '0004_alter_comments_author_user_alter_comments_issue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='appsoftdesk.issues'),
        ),
        migrations.AlterField(
            model_name='issues',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='appsoftdesk.projects'),
        ),
    ]
