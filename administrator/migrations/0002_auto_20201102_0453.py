# Generated by Django 3.1.2 on 2020-11-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmachine',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=15),
        ),
    ]
