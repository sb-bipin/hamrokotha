# Generated by Django 4.1.2 on 2022-11-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='fullname',
            field=models.CharField(max_length=122),
        ),
    ]
