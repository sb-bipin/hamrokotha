# Generated by Django 4.1.2 on 2022-11-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=False, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=121)),
            ],
        ),
    ]
