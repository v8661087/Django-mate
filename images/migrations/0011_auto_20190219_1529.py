# Generated by Django 2.1.4 on 2019-02-19 07:29

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20190215_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'left'], force_format='JPEG', keep_meta=True, quality=100, size=[750, 750], upload_to='images/%Y/%m/%d', verbose_name='相片'),
        ),
    ]
