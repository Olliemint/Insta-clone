# Generated by Django 4.0.5 on 2022-06-07 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igclone', '0008_remove_feed_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igclone.feed'),
        ),
    ]
