# Generated by Django 3.1.4 on 2022-01-24 17:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date_echeance',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 24, 17, 43, 57, 524479, tzinfo=utc), null=True),
        ),
    ]
