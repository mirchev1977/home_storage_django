# Generated by Django 3.1.4 on 2020-12-11 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userlogged'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlogged',
            old_name='createdAt',
            new_name='created_at',
        ),
    ]
