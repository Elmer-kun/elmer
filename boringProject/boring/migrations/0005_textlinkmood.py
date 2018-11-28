# Generated by Django 2.1.1 on 2018-09-27 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('boring', '0004_auto_20180925_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='textLinkMood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=150)),
                ('createDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]