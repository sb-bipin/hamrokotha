# Generated by Django 4.1.2 on 2022-11-20 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='username',
        ),
    ]
