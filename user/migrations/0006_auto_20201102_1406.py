# Generated by Django 3.1.2 on 2020-11-02 14:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201102_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmcard',
            name='date_issued',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='atmcard',
            name='expire_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
