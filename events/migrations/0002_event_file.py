# Generated by Django 5.1.2 on 2024-10-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='fichier HelloAsso'),
        ),
    ]
