# Generated by Django 3.1.1 on 2020-09-28 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20200928_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 10, 57, 19, 921448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='uuid',
            field=models.CharField(default='6c759e55d823', editable=False, max_length=64),
        ),
    ]
