# Generated by Django 4.0.5 on 2022-06-07 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igclone', '0002_feed_author_feed_created_feed_likes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='comments',
        ),
        migrations.AlterField(
            model_name='feed',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
