# Generated by Django 4.1.2 on 2023-04-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_alter_contact_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='descp',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='propertytype',
            field=models.CharField(choices=[('Rooms', 'Rooms'), ('Flat', 'Flat'), ('House', 'House'), ('Others', 'Others')], default='Others', max_length=10),
        ),
    ]
