# Generated by Django 3.1.2 on 2020-10-14 05:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20201014_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscription',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscriber', to=settings.AUTH_USER_MODEL, verbose_name='Подписка'),
        ),
    ]
