# Generated by Django 5.1.2 on 2024-10-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateField(verbose_name='Date')),
                ('event_start_time', models.TimeField(verbose_name='Start Time')),
                ('event_end_time', models.TimeField(verbose_name='End Time')),
                ('event_location', models.CharField(max_length=200, verbose_name='Address')),
                ('event_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('event_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Image')),
                ('event_outdoor', models.BooleanField(default=False, verbose_name='Outdoor')),
            ],
        ),
    ]