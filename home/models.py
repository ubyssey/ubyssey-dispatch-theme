from . import blocks as homeblocks

from article.models import ArticlePage
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

# Create your models here.

class HomePage(Page):
    template = "home/home_page.html"
    
    parent_page_types = [
        'wagtailcore.Page',
    ]

    subpage_types = [
        'section.SectionPage',
        'authors.AllAuthorsPage',
    ]

    sections_stream = StreamField(
        [
            ("home_page_section_block",homeblocks.HomePageSectionBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("sections_stream", heading="Sections"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['above_cut_articles'] = self.get_above_cut_articles(max_count=6)
        return context

    def get_above_cut_articles(self, max_count=6):
        return ArticlePage.objects.all().order_by('-last_published_at')[:max_count]

    above_cut_articles = property(fget=get_above_cut_articles)