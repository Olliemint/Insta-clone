# Generated by Django 4.0.5 on 2022-06-07 19:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('igclone', '0010_feed_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='feed_post', to=settings.AUTH_USER_MODEL),
        ),
    ]