# Generated by Django 2.1.4 on 2019-01-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190108_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='mate/media/default.jpg', upload_to='users/%Y/%m/%d'),
        ),
    ]