
import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'vsfygxju9)=k8qxmc9!__ng%dooyn-w7il_z+w)grvkz4ks!)u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.humanize.apps.HumanizeConfig",
    "django.contrib.auth.apps.AuthConfig",
    "django.contrib.contenttypes.apps.ContentTypesConfig",
    "django.contrib.sessions.apps.SessionsConfig",
    "django.contrib.sites.apps.SitesConfig",
    "django.contrib.messages.apps.MessagesConfig",
    "django.contrib.staticfiles.apps.StaticFilesConfig",
    "django.contrib.admin.apps.AdminConfig",
    "django.contrib.admindocs.apps.AdminDocsConfig",
    "sekizai",
    "sorl.thumbnail",
    "django_nyt.apps.DjangoNytConfig",
    "wiki.apps.WikiConfig",
    "wiki.plugins.macros.apps.MacrosConfig",
    "wiki.plugins.help.apps.HelpConfig",
    "wiki.plugins.links.apps.LinksConfig",
    "wiki.plugins.images.apps.ImagesConfig",
    "wiki.plugins.attachments.apps.AttachmentsConfig",
    "wiki.plugins.notifications.apps.NotificationsConfig",
    "wiki.plugins.editsection.apps.EditSectionConfig",
    "wiki.plugins.globalhistory.apps.GlobalHistoryConfig",
    "mptt",
]


MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
]
SITE_ID=1

ROOT_URLCONF = 'wikidj.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
            "debug": DEBUG,
        },
    },
]
WSGI_APPLICATION = 'wikidj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


WIKI_ANONYMOUS_WRITE = True
WIKI_ANONYMOUS_CREATE = False
LOGIN_REDIRECT_URL = reverse_lazy('wiki:get', kwargs={'path': ''})



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)