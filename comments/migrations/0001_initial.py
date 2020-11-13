# Generated by Django 3.1.2 on 2020-11-12 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publications', '0004_auto_20201112_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('publication_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='publications.publication', verbose_name='Публикация')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='от кого')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_to_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='comments.comment', verbose_name='На комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_to_comment_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='comments.comment_to_comment', verbose_name='Какому комментарию (на комментарий)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_to_comment_like', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='comments.comment', verbose_name='Какому комментарию')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to=settings.AUTH_USER_MODEL, verbose_name='От кого')),
            ],
        ),
    ]