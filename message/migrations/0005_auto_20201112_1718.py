# Generated by Django 3.1.2 on 2020-11-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_auto_20201112_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageimage',
            name='image',
            field=models.ImageField(upload_to='message_image'),
        ),
    ]
