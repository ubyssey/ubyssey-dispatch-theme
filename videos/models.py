from django.db import models
from django.utils import timezone

from django_extensions.db.fields import AutoSlugField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager

from ubyssey.validators import validate_youtube_url

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet

#-----Taggit stuff-----

class VideoTag(TaggedItemBase):
    content_object = ParentalKey('videos.VideoSnippet', on_delete=models.CASCADE, related_name='tagged_items')

#-----Orderable models-----

class VideoAuthorsOrderable(Orderable):
    """
    This closely corresponds to the Dispatch model that is (mis-)named "Author"
    """
    video = ParentalKey(
        "videos.VideoSnippet",
        related_name="video_authors",
    )
    author = models.ForeignKey(
        'authors.AuthorPage',
        on_delete=models.CASCADE,
    )
    panels = [
        MultiFieldPanel(
            [
                PageChooserPanel("author"),
            ],
            heading="Author",
        ),
    ]

#-----Snippet models-----

@register_snippet
class VideoSnippet(ClusterableModel):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default='',
    )
    slug = AutoSlugField(
        populate_from="title",
        editable=True,
        max_length=255,
        primary_key=True,
        unique=True,
        db_index=True,
        null=False,
        blank=False,
        default='',
    )
    url = models.URLField(
        max_length=500,
        null=False,
        blank=False,
        default='',
        validators=[validate_youtube_url,]
    )

    # authors = ManyToManyField(Author, related_name='video_authors')
    tags = TaggableManager(through=VideoTag, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("title"), 
                FieldPanel("slug"),
                FieldPanel("url"),
            ],
            heading="Necessary Fields"
        ),
        MultiFieldPanel(
            [
                InlinePanel("video_authors", max_num=20, label="Author"),
            ],
            heading="Author(s)"
        ),
        MultiFieldPanel(
            [
                FieldPanel("tags"), 
            ],
            heading="Tags"
        ),
    ]
    
    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
