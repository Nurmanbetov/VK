# Generated by Django 3.1.2 on 2020-10-25 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20201025_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default-profile.jpg', null=True, upload_to='images', verbose_name='Фото профиля'),
        ),
    ]
