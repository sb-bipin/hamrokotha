# Generated by Django 4.2 on 2023-06-19 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_property_remove_rooms_address_remove_rooms_descp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default=None, max_length=10)),
                ('totalrooms', models.CharField(default=None, max_length=3)),
                ('property', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Flats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wifiavailable', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5)),
                ('totalrooms', models.CharField(default=None, max_length=3)),
                ('property', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='home.property')),
            ],
        ),
    ]
