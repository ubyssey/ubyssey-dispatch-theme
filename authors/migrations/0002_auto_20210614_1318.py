# Generated by Django 3.1.12 on 2021-06-14 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0063_auto_20210614_1318'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllAuthorsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AuthorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('full_name', models.CharField(max_length=255)),
                ('ubyssey_role', models.CharField(blank=True, default='', max_length=255)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='authorsnippet',
            name='image',
        ),
    ]
