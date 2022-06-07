# Generated by Django 4.0.5 on 2022-06-07 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igclone', '0006_remove_feed_comments_alter_comment_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='user_post', to='igclone.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='feed',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='igclone.feed'),
        ),
    ]
