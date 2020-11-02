# Generated by Django 3.1.2 on 2020-11-02 14:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201102_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmcard',
            name='date_issued',
            field=models.DateField(default=datetime.datetime(2020, 11, 2, 14, 6, 11, 442590, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='atmcard',
            name='expire_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 2, 14, 6, 11, 442616, tzinfo=utc)),
        ),
    ]