# Generated by Django 5.0.6 on 2024-10-08 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='cog',
            new_name='id',
        ),
    ]
