# Generated by Django 5.0.7 on 2024-09-04 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('bio', models.TextField(blank=True, null=True)),
                ('course', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('national_id', models.PositiveBigIntegerField(unique=True)),
                ('account_number', models.PositiveIntegerField(unique=True)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('department', models.CharField(max_length=30)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
