# Generated by Django 4.1.7 on 2023-08-22 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('created_at', models.TimeField(auto_now=datetime.datetime(2023, 8, 22, 6, 27, 14, 66934, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
