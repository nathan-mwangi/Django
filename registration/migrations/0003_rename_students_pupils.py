# Generated by Django 5.0.3 on 2024-04-16 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Pupils',
        ),
    ]
