# Generated by Django 4.1.2 on 2022-11-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_signup_password_remove_signup_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.TextField(max_length=122),
        ),
    ]