# Generated by Django 3.1 on 2020-12-29 00:09

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EconomicNumberHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economic_number_initial', models.CharField(max_length=50, verbose_name='Initial number initial')),
                ('number', models.IntegerField(verbose_name='Number secuence')),
                ('economic_number', models.CharField(max_length=100, verbose_name='Economic number')),
            ],
        ),
        migrations.CreateModel(
            name='Van',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('plates', models.CharField(max_length=100, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_plates', message='The plates dont have the correct format', regex='^([A-Za-z]|[0-9]){3}-[0-9]{3}$')], verbose_name='Plates')),
                ('economic_number', models.CharField(max_length=100, unique=True, verbose_name='Economic number')),
                ('seats', models.IntegerField(verbose_name='Seats')),
                ('status', models.CharField(choices=[('ACTIVE', 'Activa'), ('REPAIR', 'En reparación')], max_length=70, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Udpated at')),
            ],
        ),
    ]
