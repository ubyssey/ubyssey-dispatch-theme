# Generated by Django 3.1.12 on 2021-06-29 02:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20210628_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='featured_video',
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='content',
            field=wagtail.core.fields.StreamField([('richtext', wagtail.core.blocks.RichTextBlock(help_text='Write your article contents here. See documentation: https://docs.wagtail.io/en/latest/editor_manual/new_pages/creating_body_content.html#rich-text-fields', label='Rich Text Block')), ('plaintext', wagtail.core.blocks.TextBlock(help_text='Warning: Rich Text Blocks preferred! Plain text primarily exists for importing old Dispatch text.', label='Plain Text Block')), ('dropcap', wagtail.core.blocks.TextBlock(help_text='DO NOT USE - Legacy block. Create a block where special dropcap styling with be applied to the first letter and the first letter only.\n\nThe contents of this block will be enclosed in a <p class="drop-cap">...</p> element, allowing its targetting for styling.\n\nNo RichText allowed.', label='Dropcap Block', template='article/stream_blocks/dropcap.html')), ('video', wagtail.core.blocks.StructBlock([('video_embed', wagtail.embeds.blocks.EmbedBlock(blank=False, null=False)), ('title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('credit', wagtail.core.blocks.CharBlock(max_length=255, required=False))], help_text='Use this to credit or caption videos that will only be associated with this current article, rather than entered into our video library. You can also embed videos in a Rich Text Block.', label='Credited/Captioned One-Off Video')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('default', 'Default'), ('left', 'Left'), ('right', 'Right')])), ('width', wagtail.core.blocks.ChoiceBlock(choices=[('full', 'Full'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')])), ('caption', wagtail.core.blocks.CharBlock(max_length=255, required=False)), ('credit', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('raw_html', wagtail.core.blocks.RawHTMLBlock(help_text="WARNING: DO NOT use this unless you really know what you're doing!", label='Raw HTML Block')), ('quote', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.CharBlock(required=False)), ('source', wagtail.core.blocks.CharBlock(required=False))], label='Pull Quote', template='article/stream_blocks/quote.html'))], blank=True, null=True),
        ),
    ]