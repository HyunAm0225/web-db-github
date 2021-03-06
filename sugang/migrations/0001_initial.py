# Generated by Django 3.1.1 on 2020-10-30 00:55

from django.db import migrations, models
import django.db.models.deletion
import sugang.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(blank=True, max_length=15, verbose_name='학수번호')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='과목이름')),
                ('point', models.BinaryField(blank=True, verbose_name='학점')),
                ('max_student', models.CharField(blank=True, max_length=15, verbose_name='정원')),
                ('class_time', models.CharField(blank=True, max_length=15, verbose_name='강의시간')),
                ('pd_name', models.CharField(blank=True, max_length=15, verbose_name='교수')),
                ('class_room', models.CharField(blank=True, max_length=15, verbose_name='강의실')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Sugang_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=15, verbose_name='학번')),
                ('name', models.CharField(blank=True, max_length=30, verbose_name='이름')),
                ('image', sugang.fields.ThumbnailImageField(upload_to='photo/%Y/%m', verbose_name='IMAGE')),
                ('Subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sugang.subject')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
