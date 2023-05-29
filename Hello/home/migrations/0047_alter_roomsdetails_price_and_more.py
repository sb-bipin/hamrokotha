# Generated by Django 4.2 on 2023-05-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_alter_roomsdetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomsdetails',
            name='price',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='roomsdetails',
            name='wifiavailable',
            field=models.CharField(choices=[('Yes', 'No'), ('No', 'No')], default='No', max_length=5),
        ),
    ]