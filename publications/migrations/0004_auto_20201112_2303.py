# Generated by Django 3.1.2 on 2020-11-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_comment_comment_like_comment_to_comment_comment_to_comment_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment_like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment_to_comment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment_to_comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment_to_comment_like',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment_to_comment_like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Comment_like',
        ),
        migrations.DeleteModel(
            name='Comment_to_comment',
        ),
        migrations.DeleteModel(
            name='Comment_to_comment_like',
        ),
    ]