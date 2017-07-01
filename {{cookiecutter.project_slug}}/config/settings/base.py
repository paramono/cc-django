"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
from pathlib import Path

import environ

{% if cookiecutter.cms != 'None' -%}
gettext = lambda s: s  # noqa
{%- endif %}

SETTINGS_FILE = Path(os.path.abspath(__file__))  # <root>/{{cookiecutter.project_slug}}/config/settings/base.py
SETTINGS_ROOT = SETTINGS_FILE.parents[0]  # <root>/{{cookiecutter.project_slug}}/config/settings/
CONFIGURATION_ROOT = SETTINGS_FILE.parents[1]  # <root>/{{cookiecutter.project_slug}}/config/
# REPOSITORY_ROOT = SETTINGS_FILE.parents[2]
PROJECT_ROOT = SETTINGS_FILE.parents[2]  # <root>/{{cookiecutter.project_slug}}/
COMMON_ROOT = SETTINGS_FILE.parents[3]  # <root>/

# <root>/{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}/
MAINAPP_ROOT = PROJECT_ROOT / '{{cookiecutter.project_slug}}'

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(PROJECT_ROOT / '.env')
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = [
{% if cookiecutter.cms == 'djangocms' %}
    'djangocms_admin_style',
{% endif %}
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
]

{% if cookiecutter.cms == 'djangocms' %}
CMS_APPS = [
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
{% if cookiecutter.use_djangocms_slick == 'y' %}
    'cmsplugin_slick',
{% endif %}
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'aldryn_bootstrap3',
]
{% elif cookiecutter.cms == 'wagtail' %}
CMS_APPS = [
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',
]
{% endif %}

THIRD_PARTY_APPS = [
    'crispy_forms',  # Form layouts
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'djangobower',
{% if cookiecutter.cms == 'wagtail' %}
    'taggit',
    'modelcluster',
{% endif %}
]

# Apps specific for this project go here.
LOCAL_APPS = [
    # custom users app
{% if cookiecutter.cms == 'wagtail' %}
    'home',
{% endif %}
    '{{ cookiecutter.project_slug }}.users.apps.UsersConfig',
    # Your stuff: custom apps go here
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
{% if cookiecutter.cms == 'djangocms' -%}
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + CMS_APPS
{% elif cookiecutter.cms == 'wagtail' -%}
INSTALLED_APPS = LOCAL_APPS + CMS_APPS + THIRD_PARTY_APPS + DJANGO_APPS
{% else %}
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
{%- endif %}

BOWER_COMPONENTS_ROOT = str(PROJECT_ROOT)
BOWER_INSTALLED_APPS = (
    'bootstrap-sass#3.3.7',
    # 'bootstrap#4.0.0-alpha.6',
    'jquery#2',
    'jquery-validation#1.15.0',
    # 'font-awesome',
    'slick-carousel#1.6.0',
    'matchheight#0.7.2',
)

TAGGIT_CASE_INSENSITIVE = True

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
{% if cookiecutter.cms == 'djangocms' %}
    'cms.middleware.utils.ApphookReloadMiddleware',
{%- endif %}
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
{% if cookiecutter.cms == 'djangocms' %}
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
{% elif cookiecutter.cms == 'wagtail' %}
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
{%- endif %}
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': '{{ cookiecutter.project_slug }}.contrib.sites.migrations'
}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(MAINAPP_ROOT / 'fixtures'),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [
    ("""{{cookiecutter.author_name}}""", '{{cookiecutter.email}}'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

{% if cookiecutter.cms == 'wagtail' %}
WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = '{{cookiecutter.email}}'
{% endif %}

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://{% if cookiecutter.windows == 'y' %}localhost{% endif %}/{{cookiecutter.project_slug}}'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True


# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{ cookiecutter.timezone }}'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'ru'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(MAINAPP_ROOT / 'templates'),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            {% if cookiecutter.cms == 'djangocms' %}
                'django.template.context_processors.csrf',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings'
            {%- endif %}
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(COMMON_ROOT / '{{cookiecutter.project_slug}}_static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(MAINAPP_ROOT / 'static'),
    str(PROJECT_ROOT / 'bower_components'),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(COMMON_ROOT / '{{cookiecutter.project_slug}}_media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# PASSWORD STORAGE SETTINGS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# email-only auth
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.users.adapters.AccountAdapter'
# ACCOUNT_SIGNUP_FORM_CLASS = 'teachfm.users.forms.SignupForm'
SOCIALACCOUNT_ADAPTER = '{{cookiecutter.project_slug}}.users.adapters.SocialAccountAdapter'
SOCIALACCOUNT_AUTO_SIGNUP = False

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_URL = 'account_login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
{% if cookiecutter.use_celery == 'y' %}
########## CELERY
INSTALLED_APPS += ['{{cookiecutter.project_slug}}.taskapp.celery.CeleryConfig']
CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='django://')
if CELERY_BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL
########## END CELERY
{% endif %}

{%- if cookiecutter.use_compressor == 'y'-%}
# django-compressor
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['compressor']
STATICFILES_FINDERS += ['compressor.finders.CompressorFinder']

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    # ('text/less', 'lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss --style compressed {infile} {outfile}'),
    # ('text/stylus', 'stylus < {infile} > {outfile}'),
    # ('text/foobar', 'path.to.MyPrecompilerFilter'),
)
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]
{% endif %}

{% if cookiecutter.use_sorl_thumbnail == 'y' -%}
INSTALLED_APPS += ['sorl.thumbnail']
THUMBNAIL_PRESERVE_FORMAT = True
{%- endif %}

{% if cookiecutter.use_admin_sortable2 == 'y' -%}
INSTALLED_APPS += ['adminsortable2']
{%- endif %}

# Location of root django.contrib.admin URL, use {% raw %}{% url 'admin:index' %}{% endraw %}
ADMIN_URL = r'^admin/'


# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------

LANGUAGES = {% if cookiecutter.cms == 'wagtail' %}[{% else %}({% endif %}
    ## Customize this
    ('ru', gettext('ru')),
{% if cookiecutter.multiple_languages == 'y' %}
    ('en', gettext('en')),
{% endif %}
{% if cookiecutter.cms == 'wagtail' %}]{% else %}){% endif %}

{% if cookiecutter.cms == 'wagtail' %}
WAGTAILADMIN_PERMITTED_LANGUAGES = LANGUAGES
WAGTAIL_SITE_NAME = '{{cookiecutter.project_name}}'
{% endif %}

{% if cookiecutter.cms == 'djangocms' -%}
CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'fallbacks': ['ru', 'en'],
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
    1: [
        {
            'code': 'ru',
            'name': gettext('ru'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
{% if cookiecutter.multiple_languages == 'y' %}
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
{% endif %}
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('pages/page.html', 'Базовая страница'),
    ('pages/home.html', 'Главная'),
    ('pages/contact.html', 'Контакты'),
    ('pages/masterclass/masterclass_detail.html', 'Мастер-класс'),
    ('pages/masterclass/masterclass_list.html', 'Cписок мастер-классов'),
    # ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True


def make_text_plugin(body):
    plugin = {
        'plugin_type': 'TextPlugin',
        'values': {
            'body': '%s' % body
        },
    }
    return plugin


CMS_EMPTY_TEXT_PLUGIN = make_text_plugin('<p></p>')

ALDRYN_BOOTSTRAP3_PLUGINS = [
    "Bootstrap3RowCMSPlugin",
    "Bootstrap3ColumnCMSPlugin",
    "Bootstrap3BlockquoteCMSPlugin",
    "Bootstrap3CiteCMSPlugin",
    "Bootstrap3CodeCMSPlugin",
    "Bootstrap3ButtonCMSPlugin",
    "Bootstrap3ImageCMSPlugin",
    "Bootstrap3ResponsiveCMSPlugin",
    "Bootstrap3IconCMSPlugin",
    "Bootstrap3LabelCMSPlugin",
    "Bootstrap3JumbotronCMSPlugin",
    "Bootstrap3AlertCMSPlugin",
    "Bootstrap3ListGroupCMSPlugin",
    "Bootstrap3ListGroupItemCMSPlugin",
    "Bootstrap3PanelCMSPlugin",
    "Bootstrap3PanelHeadingCMSPlugin",
    "Bootstrap3PanelBodyCMSPlugin",
    "Bootstrap3PanelFooterCMSPlugin",
    "Bootstrap3WellCMSPlugin",
    "Bootstrap3TabCMSPlugin",
    "Bootstrap3TabItemCMSPlugin",
    "Bootstrap3AccordionCMSPlugin",
    "Bootstrap3AccordionItemCMSPlugin",
    # "CarouselBase",
    # "CarouselSlideBase",
    "Bootstrap3CarouselCMSPlugin",
    "Bootstrap3CarouselSlideCMSPlugin",
    "Bootstrap3CarouselSlideFolderCMSPlugin",
    "Bootstrap3SpacerCMSPlugin",
    "Bootstrap3FileCMSPlugin",
]

CMS_PLACEHOLDER_CONF = {
    None: {
        'excluded_plugins': [
            'Bootstrap3BlockquoteCMSPlugin',
            "Bootstrap3CodeCMSPlugin",
            "Bootstrap3ImageCMSPlugin",
            "Bootstrap3JumbotronCMSPlugin",
            "Bootstrap3ListGroupCMSPlugin",
            "Bootstrap3ListGroupItemCMSPlugin",
            "Bootstrap3PanelCMSPlugin",
            "Bootstrap3PanelHeadingCMSPlugin",
            "Bootstrap3PanelBodyCMSPlugin",
            "Bootstrap3PanelFooterCMSPlugin",
            "Bootstrap3WellCMSPlugin",
            "Bootstrap3TabCMSPlugin",
            "Bootstrap3TabItemCMSPlugin",
            "Bootstrap3AccordionCMSPlugin",
            "Bootstrap3AccordionItemCMSPlugin",
            "Bootstrap3CarouselCMSPlugin",
            "Bootstrap3CarouselSlideCMSPlugin",
            "Bootstrap3CarouselSlideFolderCMSPlugin",
            "Bootstrap3SpacerCMSPlugin",
            "FilerFilePlugin",
            "FilerFolderPlugin",
            "MultiColumnPlugin",
            "VideoPlayerPlugin",
            "GoogleMapPlugin",
        ],
    },
    'content': {
        # 'excluded_plugins': ['Bootstrap3BlockquoteCMSPlugin'],
    },
    'example': {
        'name': "Example",
        'default_plugins': [{
            'plugin_type': 'TextPlugin',
            'values': {
                'body': '<p>Example</p>'
            },
        }]
    },
}
MIGRATION_MODULES = {
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

CKEDITOR_SETTINGS = {
    'language': 'ru',
    'stylesSet': 'default:/static/js/addons/ckeditor.wysiwyg.js',
    # 'contentsCss': ['/static/css/base.css'],
    # 'toolbar': 'CMS',
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', 'cmswidget', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
    'contentsCss': ['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
}
{%- endif %}
