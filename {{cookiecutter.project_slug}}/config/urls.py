{% if cookiecutter.cms == 'djangocms' -%}
from cms.sitemaps import CMSSitemap
{%- endif %}

from django.conf import settings
from django.conf.urls import include, url
{% if cookiecutter.multiple_languages == 'y' %}
from django.conf.urls.i18n import i18n_patterns
{% endif %}
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView
from django.views import defaults as default_views

{% if cookiecutter.cms == 'djangocms' -%}
admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]
{% else %}
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('{{ cookiecutter.project_slug }}.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here


]
{%- endif %}

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]


{% if cookiecutter.cms == 'djangocms' -%}
{% if cookiecutter.multiple_languages %}urlpatterns += i18n_patterns({% else %}urlpatterns += [{% endif %}
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    # url(r'^reviews/', include('reviews.urls', namespace='reviews')),  # NOQA
    # url(r'^', include('djangocms_forms.urls')),
    url(r'^', include('cms.urls')),
{% if cookiecutter.multiple_languages == 'y' %}){% else %}]{% endif %}
{%- endif %}
