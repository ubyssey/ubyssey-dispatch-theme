# Generated by Django 3.1.8 on 2021-05-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210527_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='legacy_published_at_time',
            field=models.DateTimeField(default=(1918, 10, 17, 0, 0, 0, 3, 290, -1), null=True),
        ),
    ]
