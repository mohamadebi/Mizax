# Generated by Django 4.2.1 on 2023-05-09 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='created',
            new_name='opentime',
        ),
    ]