# Generated by Django 4.2.3 on 2023-08-12 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='person',
            new_name='human',
        ),
    ]
