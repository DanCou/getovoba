# Generated by Django 5.1.2 on 2024-11-02 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_remove_player_id_alter_player_slug'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.datetime(1900, 1, 1, 0, 0), unique=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='player',
            name='firstname',
            field=models.CharField(default='James', max_length=50, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='player',
            name='lastname',
            field=models.CharField(default='Bond', max_length=50, verbose_name='Nom'),
        ),
        migrations.AddConstraint(
            model_name='player',
            constraint=models.UniqueConstraint(fields=('lastname', 'firstname', 'birthday'), name='unique_player'),
        ),
    ]
