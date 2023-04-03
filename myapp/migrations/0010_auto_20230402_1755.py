# Generated by Django 3.2.18 on 2023-04-02 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_video_creator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='video',
            name='dislikes_counter',
        ),
        migrations.RemoveField(
            model_name='video',
            name='likes_counter',
        ),
        migrations.RemoveField(
            model_name='video',
            name='popularity',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
    ]