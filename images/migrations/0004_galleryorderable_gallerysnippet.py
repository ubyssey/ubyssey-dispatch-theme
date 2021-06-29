# Generated by Django 3.1.12 on 2021-06-29 02:38

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_ubysseyimage_legacy_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='GallerySnippet',
            fields=[
                ('title', models.TextField()),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleryOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.TextField(blank=True, default='')),
                ('credit', models.TextField(blank=True, default='')),
                ('gallery', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='images.gallerysnippet')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.ubysseyimage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]