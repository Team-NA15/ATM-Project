# Generated by Django 3.1.2 on 2020-11-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_auto_20201103_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
