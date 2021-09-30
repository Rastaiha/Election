# Generated by Django 3.1.1 on 2021-09-30 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_auto_20201001_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 15, 36, 22, 676959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 15, 36, 22, 685039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('42ffc9ba-ec12-424c-b196-4b474d913342'), editable=False),
        ),
    ]
