# Generated by Django 4.2.2 on 2023-06-13 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0003_mark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mark',
            old_name='riddle',
            new_name='collect',
        ),
    ]
