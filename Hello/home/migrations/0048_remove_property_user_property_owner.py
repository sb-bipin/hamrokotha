# Generated by Django 4.2 on 2023-08-19 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0047_property_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='user',
        ),
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
