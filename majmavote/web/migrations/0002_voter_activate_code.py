# Generated by Django 3.1.1 on 2020-09-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='activate_code',
            field=models.CharField(blank=True, default=' ', max_length=5),
        ),
    ]