# Generated by Django 4.2.3 on 2023-08-12 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_person_human'),
    ]

    operations = [
        migrations.RenameField(
            model_name='human',
            old_name='pancard_id',
            new_name='pancard',
        ),
    ]