# Generated by Django 3.1.3 on 2020-11-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_auto_20201120_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default-profile.jpg', null=True, upload_to='', verbose_name='Profile photo'),
        ),
    ]
