# Generated by Django 2.2.1 on 2019-07-15 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20190715_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='lastQuestion',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 18, 9, 22, 788675)),
        ),
    ]
