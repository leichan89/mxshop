# Generated by Django 3.0.7 on 2020-07-01 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLeavingMeaasge',
            new_name='UserLeavingMessage',
        ),
    ]
