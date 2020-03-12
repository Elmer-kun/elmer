# Generated by Django 2.2.6 on 2020-03-12 09:59

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClockText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('clockInfo', models.CharField(max_length=200)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserClockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('clockInfo', models.CharField(max_length=200)),
                ('startTime', models.DateTimeField(default=datetime.datetime(2020, 3, 12, 9, 59, 4, 841487))),
                ('endTime', models.DateTimeField(default=datetime.datetime(2020, 3, 12, 9, 59, 4, 841487))),
                ('clockLen', models.IntegerField(default=0)),
            ],
        ),
    ]
