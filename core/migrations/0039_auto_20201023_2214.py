# Generated by Django 3.1.2 on 2020-10-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20201023_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/static/default-profile.jpg', null=True, upload_to='media/progile_image', verbose_name='Фото профиля'),
        ),
    ]
