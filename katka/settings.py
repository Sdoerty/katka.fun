from pathlib import Path
import os, psycopg2

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# Путь используется для определения базоового шаблона base_katka.html
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's4qiuu9o3jg=l!7k2lwt17tkc!6aye+ms(at&n(m%b^tsz5yt6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

# Вместо User теперь использовать свою модель - AUTH_USER_MODEL---------------------------------------------
AUTH_USER_MODEL = 'signup.Account'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'login.backends.CaseInsensitiveModelBackend',
    )

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'login.apps.AuthRegConfig',
    'signup.apps.SignupConfig',
    'main.apps.MainpageConfig',
    'katkamessages.apps.KatkamessagesConfig',
    'profile.apps.UserProfileConfig',
    'users.apps.UsersConfig',
    'messenger',
    'multiselectfield',
    'friendship',
    'channels',
    'crispy_forms',
]

ASGI_APPLICATION = "katka.asgi.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'katka.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, "katka/base_templates/")
LOGIN_TEMPLATE = os.path.join(BASE_DIR, 'login/templates/login/')
SIGNUP_TEMPLATE = os.path.join(BASE_DIR, 'signup/templates/signup/')
PROFILE_TEMPLATE = os.path.join(BASE_DIR, 'profile/templates/profile')
EDIT_PROFILE_TEMPLATE = os.path.join(BASE_DIR, 'profile/templates/edit_profile')
KATKA_PAGE = os.path.join(BASE_DIR, 'main/templates/katka_page')
CREATE_KATKA = os.path.join(BASE_DIR, 'main/templates/create_katka')
ALL_KATKA = os.path.join(BASE_DIR, 'main/templates/main')
ALL_USERS = os.path.join(BASE_DIR, 'users/templates/users')
SOME_USER = os.path.join(BASE_DIR, 'users/templates/some')
MESSENGER = os.path.join(BASE_DIR, 'messenger/templates/messenger')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, LOGIN_TEMPLATE, SIGNUP_TEMPLATE, PROFILE_TEMPLATE, EDIT_PROFILE_TEMPLATE, KATKA_PAGE,
                 CREATE_KATKA, ALL_USERS, SOME_USER, ALL_KATKA],
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


WSGI_APPLICATION = 'katka.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'k1',
        'USER': 'romero',
        'PASSWORD': '2580654',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "katka/static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CRISPY_TEMPLATE_PACK='bootstrap4'
BASE_URL = "http://127.0.0.1:8000"
