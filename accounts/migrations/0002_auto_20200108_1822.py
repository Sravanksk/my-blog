# Generated by Django 3.0.2 on 2020-01-08 18:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserModel',
            new_name='UserProfile',
        ),
    ]
