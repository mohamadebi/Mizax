# Generated by Django 4.2.1 on 2023-05-09 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_created_place_opentime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='country',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='pupulation',
            new_name='ticket_price',
        ),
    ]