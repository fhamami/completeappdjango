# Generated by Django 2.0.2 on 2018-02-22 04:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': 'home'},
        ),
        migrations.AlterField(
            model_name='home',
            name='date_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 2, 22, 4, 19, 17, 330693, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
