# Generated by Django 3.1.1 on 2020-09-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200928_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='voters',
            field=models.ManyToManyField(to='web.Voter'),
        ),
    ]