# Generated by Django 3.1.2 on 2020-10-23 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20201023_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/default-profile.jpg', null=True, upload_to='profile', verbose_name='Фото профиля'),
        ),
    ]
