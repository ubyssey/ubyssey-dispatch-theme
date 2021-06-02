# Generated by Django 3.1.8 on 2021-05-28 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20210527_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='articlepage',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(1918, 10, 17, 0, 0), help_text='To be explicitly shown to the reader. Defaults to today. Articles are seperately date/timestamped for database use, so editors can explicitly override the displayed date.'),
        ),
    ]