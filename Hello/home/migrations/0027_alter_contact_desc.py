# Generated by Django 4.1.2 on 2023-04-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_remove_image_propertytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]