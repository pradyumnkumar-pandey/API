# Generated by Django 4.0.6 on 2022-09-09 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='role',
            new_name='role_user',
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
    ]
