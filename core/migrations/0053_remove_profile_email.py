# Generated by Django 3.1.2 on 2020-10-28 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20201028_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]