# Generated by Django 4.2.3 on 2023-08-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_pancard_id_human_pancard'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='human',
            name='address',
        ),
    ]