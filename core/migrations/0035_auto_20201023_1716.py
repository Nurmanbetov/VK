# Generated by Django 3.1.2 on 2020-10-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20201023_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Фото профиля'),
        ),
    ]
