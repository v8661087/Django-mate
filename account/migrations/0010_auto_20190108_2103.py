# Generated by Django 2.1.4 on 2019-01-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20190108_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.jpg', upload_to='users/%Y/%m/%d'),
        ),
    ]
