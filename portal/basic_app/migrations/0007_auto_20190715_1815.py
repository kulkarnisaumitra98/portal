# Generated by Django 2.2.1 on 2019-07-15 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_auto_20190715_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='lastQuestion',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 18, 15, 42, 30327, tzinfo=utc)),
        ),
    ]
