# Generated by Django 4.2 on 2023-05-17 05:08

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_alter_image_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
