# Generated by Django 2.1.4 on 2019-03-15 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0017_comment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='comments_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
