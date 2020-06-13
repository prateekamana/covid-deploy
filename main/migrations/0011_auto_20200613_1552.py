# Generated by Django 3.0.5 on 2020-06-13 15:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200613_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='Anonymous', max_length=30),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 15, 52, 43, 266238, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 13, 15, 52, 43, 265417, tzinfo=utc)),
        ),
    ]