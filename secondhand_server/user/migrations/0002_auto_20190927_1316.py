# Generated by Django 2.2.5 on 2019-09-27 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='salt',
            new_name='third_party_token',
        ),
        migrations.RemoveField(
            model_name='user',
            name='thid_party_token',
        ),
    ]
