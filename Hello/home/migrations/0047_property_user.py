# Generated by Django 4.2 on 2023-07-12 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0046_houses_flats'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property', to=settings.AUTH_USER_MODEL),
        ),
    ]
