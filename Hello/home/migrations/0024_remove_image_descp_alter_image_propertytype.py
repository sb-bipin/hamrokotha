# Generated by Django 4.1.2 on 2023-04-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_image_descp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='descp',
        ),
        migrations.AlterField(
            model_name='image',
            name='propertytype',
            field=models.CharField(choices=[('Rooms', 'Rooms'), ('Flat', 'Flat'), ('House', 'House'), ('Others', 'Others')], default=None, max_length=10),
        ),
    ]