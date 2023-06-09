import os
from pathlib import Path
from datetime import timedelta
import cloudinary
import cloudinary.api
import cloudinary.uploader


BASE_DIR = Path(__file__).resolve().parent.parent # type: ignore


if str(os.environ.get('DJANGO_ENV')) == 'local':
    DEBUG = True
else:
    DEBUG = False
    
  
if DEBUG:
    SECRET_KEY = str(os.environ.get('LOCAL_SECRET_KEY'))
else:
    SECRET_KEY = str(os.environ.get('PRODUCTION_SECRET_KEY'))
    
    
if DEBUG:
   ALLOWED_HOSTS = [
       '127.0.0.1', 
       'localhost', 
       'honeste-backend.vercel.app'
    ] 
else:
    ALLOWED_HOSTS = [
        '.vercel.app', 
        'cfi.church', 
        'honeste-backend.vercel.app'
    ]
    

if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        'http://localhost:3000'
    ]
else:
    CORS_ALLOWED_ORIGINS = [
        'https://cfi.church',
        'https://www.cfi.church',
        'https://honeste.vercel.app',
    ]
    

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000', 
    'https://cfi.church',
    'https://www.cfi.church'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'cloudinary',
    'apps',
    'apps.users',
    'apps.churches',
    'apps.bookkeeper',
    'apps.chat',
    'apps.events',
    'apps.people',
    'apps.projects',
    'apps.resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'honeste.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'honeste.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE')),
        'NAME': str(os.environ.get('DB_NAME')),
        'HOST': str(os.environ.get('DB_HOST')),
        'PORT': str(os.environ.get('DB_PORT')),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
    },
}

print(DATABASES)


# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': str(os.environ.get('DB_ENGINE')),
#             'NAME': str(os.environ.get('DB_NAME')),
#             'HOST': str(os.environ.get('DB_HOST')),
#             'PORT': str(os.environ.get('DB_PORT')),
#             'USER': str(os.environ.get('DB_USER')),
#             'PASSWORD': str(os.environ.get('DB_PASSWORD')),
#         },
#     }


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

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Harare'

USE_I18N = True

USE_TZ = True

# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static/')
#     ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# if not DEBUG:
#     STORAGES = {
#         'staticfiles': {
#             'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
#         },
#     }


cloudinary.config( 
    cloud_name = str(os.environ.get('CLOUDINARY_NAME')), 
    api_key = str(os.environ.get('CLOUDINARY_API_KEY')), 
    api_secret = str(os.environ.get('CLOUDINARY_API_SECRET')),
)
     
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    
    "ALGORITHM": "HS256",
    "SIGNING_KEY": str(os.environ.get('JWT_SECRET_KEY')),
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
}

