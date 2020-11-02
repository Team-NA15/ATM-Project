# Generated by Django 3.1.2 on 2020-11-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('canceled', 'Canceled'), ('pending', 'Pending'), ('complete', 'Complete')], default='pending', max_length=12),
        ),
    ]