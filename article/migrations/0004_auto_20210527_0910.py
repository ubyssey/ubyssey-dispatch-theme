# Generated by Django 3.1.8 on 2021-05-27 16:10

import datetime
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210526_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='is_explicit',
            field=models.BooleanField(default=False, help_text='Check if this article contains advertiser-unfriendly content. Disables ads for this specific article.'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='last_modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='publication_date',
            field=models.DateField(default=datetime.date.today, help_text='To be explicitly shown to the reader. Defaults to today. Articles are seperately date/timestamped for database use, so editors can explicitly override the displayed date.'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='show_last_modified',
            field=models.BooleanField(default=False, help_text='Check this to alert readers the article has been revised since its publication.'),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(help_text='Write your article contents here. See documentation: https://docs.wagtail.io/en/latest/editor_manual/new_pages/creating_body_content.html#rich-text-fields', label='Rich Text Block')), ('plaintext', wagtail.core.blocks.TextBlock(help_text='Warning: Rich Text Blocks preferred! Plain text primarily exists for importing old Dispatch text.', label='Plain Text Block')), ('dropcap', wagtail.core.blocks.TextBlock(help_text='Create a block where special dropcap styling with be applied to the first letter and the first letter only.\n\nThe contents of this block will be enclosed in a <p class="drop-cap">...</p> element, allowing its targetting for styling.\n\nNo RichText allowed.', label='Dropcap Block', template='article/stream_blocks/dropcap.html')), ('video', wagtail.core.blocks.StructBlock([('video_embed', wagtail.embeds.blocks.EmbedBlock(blank=False, null=False)), ('title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('credit', wagtail.core.blocks.CharBlock(max_length=255, required=False))], help_text='Use this to credit or caption videos that will only be associated with this current article, rather than entered into our video library. You can also embed videos in a Rich Text Block.', label='Credited/Captioned One-Off Video')), ('image', wagtail.images.blocks.ImageChooserBlock(label='Image')), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text="WARNING: DO NOT use this unless you really know what you're doing!", label='Raw HTML Block'))], blank=True, null=True),
        ),
    ]
