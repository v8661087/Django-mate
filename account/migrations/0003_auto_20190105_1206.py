# Generated by Django 2.1.4 on 2019-01-05 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='使用者名稱',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='全名',
        ),
    ]
