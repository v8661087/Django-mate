# Generated by Django 2.1.4 on 2019-04-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0020_remove_image_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]
