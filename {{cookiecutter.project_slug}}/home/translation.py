{% if cookiecutter.cms == 'wagtail' %}
{% if cookiecutter.multiple_languages == 'y' %}
from .models import HomePage
from wagtail_modeltranslation.translator import WagtailTranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTr(WagtailTranslationOptions):
    fields = (
        'intro',
        'body',
    )
{% endif %}
{% endif %}
