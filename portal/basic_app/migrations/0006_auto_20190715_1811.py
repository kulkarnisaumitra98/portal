# Generated by Django 2.2.1 on 2019-07-15 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20190715_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='lastQuestion',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 18, 11, 55, 174813)),
        ),
    ]
