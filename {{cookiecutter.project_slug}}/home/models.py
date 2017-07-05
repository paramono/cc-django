{% if cookiecutter.cms == 'wagtail' %}
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class HomePage(Page):
    intro = RichTextField(blank=True)

    body = StreamField([
        ('text', blocks.RichTextBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock(template='wagtail_blocks/image.html')),
        ('document', DocumentChooserBlock()),
        ('embed', EmbedBlock(template='wagtail_blocks/embed.html')),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]
{% endif %}
