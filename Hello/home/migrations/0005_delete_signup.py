# Generated by Django 4.1.2 on 2022-11-20 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_login_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signup',
        ),
    ]
