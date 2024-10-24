# Generated by Django 5.1.2 on 2024-10-23 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_end_time',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_location',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_outdoor',
            new_name='outdoor',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_start_time',
            new_name='start_time',
        ),
    ]