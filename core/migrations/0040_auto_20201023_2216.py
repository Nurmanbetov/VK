# Generated by Django 3.1.2 on 2020-10-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20201023_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/static/default-profile.jpg', null=True, upload_to='media/profile_image', verbose_name='Фото профиля'),
        ),
    ]
