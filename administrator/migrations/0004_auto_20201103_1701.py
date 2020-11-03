# Generated by Django 3.1.2 on 2020-11-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_auto_20201102_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmachine',
            name='atm_machine_uid',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='atmachinerefill',
            name='refill_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]