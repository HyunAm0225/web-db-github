# Generated by Django 3.1.1 on 2020-11-11 07:09

from django.db import migrations
import party.fields


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_partyname_openday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='image',
            field=party.fields.ThumbnailImageField(upload_to='party/%Y/%m', verbose_name='이미지'),
        ),
    ]
