"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv  # для защиты личных данных

load_dotenv()  # получить доступ к значениям переменных среды, используя os.environ:

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_4ve7b%*tuz8fpio2j2%c=d)awx@5jhu294+o^_mt5z-vh9+#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # добавляет пользователей
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # добавляет сообщения
    'django.contrib.staticfiles',

    'new_portal',
    'news',
    'django_filters',
    'django.contrib.sites',  # # добавляет настройки сайта

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',  # поддержка входа с помощью Yandex

    'django_apscheduler',  # для собственных команд
]

SITE_ID = 1

SITE_URL = 'http://127.0.0.1:8000'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',  # Локализация

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'project.urls'

# Локализация
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # `allauth` обязательно нужен этот процессор
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'
# 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / 'new_portal' / 'static',
]

LOGIN_REDIRECT_URL = '/news'  # После входа, нас перебросит на список всех новостей

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # встроенный бэкенд Django реализующий аутентификацию по username;
    'allauth.account.auth_backends.AuthenticationBackend',  # бэкенд аутентификации, предоставленный пакетом allauth
]

ACCOUNT_EMAIL_REQUIRED = True             # поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True               # поле email является уникальным
ACCOUNT_USERNAME_REQUIRED = False         # username необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email'   # аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # верификация почты отсутствует
# Указали форму для дополнительной обработки регистрации пользователя
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}
# позволит избежать дополнительного входа и активирует аккаунт сразу, как только мы перейдём по ссылке
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# хранит количество дней, когда доступна ссылка на подтверждение регистрации
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# Настройки почты
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # для отправки писем на реальные почтовые адреса
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Для тестирования, печать писем в консоль.
EMAIL_HOST = 'smtp.yandex.ru'                                # хост почтового сервера
EMAIL_PORT = 465                                             # порт, на который почтовый сервер принимает письма
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')          # логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')  # пароль пользователя почтового сервера
EMAIL_USE_TLS = False                                    # необходимость использования TLS (зависит от почтового сервера
EMAIL_USE_SSL = True                                     # необходимость использования SSL (зависит от почтового сервера

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')  # почтовый адрес отправителя по умолчанию

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

# при новой регистрации, данному списку менеджеров будет приходить оповещение
MANAGERS = (
    ('manager', 'ServisVLG4@yandex.ru'),
)

# при новой регистрации, данному списку администраторов будет приходить оповещение
ADMINS = [
    ('administrator', 'servisvlg4@rambler.ru'),
]

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'  # формат в котором будет выполняться рассылка
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # за сколько секунд наша функция должна выполниться

# Если вы используете Redis Labs, то переменные CELERY_BROKER_URL и CELERY_RESULT_BACKEND должны строиться по шаблону:
# redis://логин:пароль@endpoint:port где endpoint и port вы также берёте из настроек Redis Labs.
CELERY_BROKER_URL = 'redis://localhost:6379'  # Указывает на URL брокера сообщений (Redis). По умолчанию порт 6379
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  # указывает на хранилище результатов выполнения задач
CELERY_ACCEPT_CONTENT = ['application/json']  # допустимый формат данных
CELERY_TASK_SERIALIZER = 'json'  # метод сериализации задач
CELERY_RESULT_SERIALIZER = 'json'  # метод сериализации результатов
# CELERY_TIMEZONE = 'Europe/Mosсow'
CELERY_ENABLE_UTC = False  # в состоянии True, задача по времени не стартовала, работала только в режиме 'каждую минуту'

# в комментарии указан номер задания (из "Итоговое задание 13.4"), к которому преминялся данный кусок словаря.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'form_debug': {
            'format': '{asctime} - [{levelname}] - {message}',
            'style': '{',
        },  # 1

        'form_warning_mail': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} ',
            'style': '{',
        },  # 1 и 5

        'form_error': {
            'format': '{asctime} - [{levelname}] - {message} - {pathname} - {exc_info} ',
            'style': '{',
        },  # 1 и 3

        'general_security_info': {
            'format': '{asctime} - [{levelname}] - {message} - {module} ',
            'style': '{',
        },  # 2 и 4
    },

    'handlers': {
        'console_d': {
            'level': 'INFO',  # DEBUG
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_debug',
        },  # 1

        'console_w': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_warning_mail',
        },  # 1

        'console_e': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'form_error',
        },  # 1

        'general_hand': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'general.log',
        },  # 2

        'errors_hand': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'form_error',
            'filename': 'errors.log',
        },  # 3

        'security_hand': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general_security_info',
            'filename': 'security.log',
        },  # 4

        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'form_warning_mail',
        },  # 5
    },

    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},  # 1 х3
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},  # 5 и 2
    },

    'loggers': {
        'django': {
            'handlers': ['console_d', 'console_w', 'console_e', 'general_hand', ],
            'level': 'DEBUG',
            'propagate': True,
        },  # 1 и 2

        'django.request': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },  # 3 и 5

        'django.server': {
            'handlers': ['errors_hand', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },  # 3 и 5

        'django.template': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.db.backends': {
            'handlers': ['errors_hand', ],
            'level': 'ERROR',
            'propagate': True,
        },  # 3

        'django.security': {
            'handlers': ['security_hand', ],
            'level': 'INFO',
            'propagate': False,
        },  # 4
    }
}

