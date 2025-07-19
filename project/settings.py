from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'accept',
    'origin',
    'user-agent',
    'accept-encoding',
]

CORS_ALLOW_METHODS = [
    'GET',
]

import os
import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {name} {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },

    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
    },

    'django': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
        'propagate': True,
    },
}


ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'cloudinary',
    'cloudinary_storage',
    'nested_admin',
    'corsheaders',
    'django_filters',

    # my apps
    'accounts.apps.AccountsConfig',
    'structure',
    'bahary_admin',
    'events',
    'news',
    'registrations',
    'activities',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'bahary_admin' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


if not DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('NAME_'),
            'USER': os.getenv('USER_'),
            'PASSWORD': os.getenv('PASSWORD_'),
            'HOST': os.getenv('HOST_'),
            'PORT': os.getenv('PORT_'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مهم للإنتاج

STATICFILES_DIRS = [
    BASE_DIR / "bahary_admin" / "static",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

JAZZMIN_SETTINGS = {
    "site_title": "Bahary Youth Admin",
    "site_header": "شباب بحري",
    "site_brand": "شباب بحري",
    "welcome_sign": "أهلاً بك في لوحة تحكم شباب بحري",
    "copyright": "جميع الحقوق محفوظة شباب بحري - Bahary Youth",
    "site_logo": "bahary_admin/images/logo B3 png.png",
    "show_sidebar": True,
    "navigation_expanded": True,
    "user_avatar": "image",
    "icons": {
        "accounts.User": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
        "structure.Governorate": "fas fa-map-marker-alt",
        "structure.CentralUnit": "fas fa-building",
        "structure.Branch": "fas fa-code-branch",
        "authtoken.Token": "fas fa-key",
        "news.News": "fas fa-newspaper",
        "news.NewsImage": "fas fa-image",
        "events.Event": "fas fa-calendar-alt",
        "admin.LogEntry": "fas fa-history",
        "events.Category": "fa-solid fa-list",
        "activities.Activities": "fa-solid fa-icons",
        "registrations.RegisterationEvents":"fa-solid fa-address-card",
        "registrations.RegisterationActivities":"fa-solid fa-address-card",
    },
}

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (26.8206, 30.8025),
    'DEFAULT_ZOOM': 6,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Bahary Youth',
}

LOGIN_REDIRECT_URL = '/admin/'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}
