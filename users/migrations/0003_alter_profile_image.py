# Generated by Django 4.0.5 on 2022-06-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.jpeg', upload_to='profilepics'),
        ),
    ]
