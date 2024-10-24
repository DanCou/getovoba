# Generated by Django 5.1.2 on 2024-10-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0002_event_event_outdoor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(verbose_name='End Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_outdoor',
            field=models.BooleanField(default=False, verbose_name='outdoor'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(verbose_name='Start Time'),
        ),
    ]
