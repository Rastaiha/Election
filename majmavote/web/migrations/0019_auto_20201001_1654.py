# Generated by Django 3.1.1 on 2020-10-01 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20200928_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='avatar',
            field=models.ImageField(default='candidate/default.png', upload_to='candidate/'),
        ),
        migrations.AlterField(
            model_name='election',
            name='expire_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 16, 54, 22, 221075, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vote',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 16, 54, 22, 222502, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='voter',
            name='uuid',
            field=models.CharField(default=uuid.UUID('14372956-d615-4e0f-9cf5-1fa2201d8f72'), editable=False, max_length=64),
        ),
    ]