from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),         # отслеживание главной страницы
    path('about/', views.about, name='about'),  # отслеживание страницы, про нас
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
]
