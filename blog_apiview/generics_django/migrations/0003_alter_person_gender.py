# Generated by Django 4.0.6 on 2022-09-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics_django', '0002_alter_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
