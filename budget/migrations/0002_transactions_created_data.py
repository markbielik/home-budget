# Generated by Django 4.0.5 on 2022-06-17 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='created_data',
            field=models.DateField(default=datetime.datetime(2022, 6, 17, 14, 56, 56, 409934, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
