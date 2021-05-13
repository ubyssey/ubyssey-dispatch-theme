# Generated by Django 3.1.8 on 2021-05-11 19:52

from django.db import migrations, models
import django.db.models.deletion
import specialfeaturelanding.blocks
import specialfeaturelanding.validators
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('dispatch_article', wagtail.core.blocks.StructBlock([('article_slug', wagtail.core.blocks.CharBlock(help_text='Type the SLUG of an article to be included here', required=True, validators=[specialfeaturelanding.validators.validate_published_article]))])), ('dispatch_article_chooser', specialfeaturelanding.blocks.DispatchArticleChooserBlock())], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]