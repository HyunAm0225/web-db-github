# Generated by Django 3.1.1 on 2020-11-06 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0005_auto_20201106_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='point',
            field=models.IntegerField(blank=True, verbose_name='학점'),
        ),
    ]
