# Generated by Django 3.1.1 on 2020-11-11 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_partyname_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partyname',
            name='openday',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='개최 날짜'),
        ),
    ]
