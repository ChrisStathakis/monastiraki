# Generated by Django 2.0.7 on 2019-04-18 08:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0004_auto_20190418_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentorders',
            name='date_expired',
            field=models.DateField(default=datetime.datetime(2019, 4, 18, 8, 2, 24, 204206, tzinfo=utc)),
        ),
    ]