# Generated by Django 3.1.1 on 2020-10-30 01:10

from django.db import migrations
import sugang.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sugang', '0002_auto_20201030_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugang_student',
            name='image',
            field=sugang.fields.ThumbnailImageField(upload_to='sugang/%Y/%m', verbose_name='IMAGE'),
        ),
    ]
