# Generated by Django 4.2.4 on 2024-05-06 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_videocall_date_ended_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocall',
            name='date_ended',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 22, 43, 3, 727843)),
        ),
        migrations.AlterField(
            model_name='videocall',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 22, 43, 3, 727843)),
        ),
    ]
