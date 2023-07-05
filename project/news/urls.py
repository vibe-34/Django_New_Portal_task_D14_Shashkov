from django.urls import path
from . import views  # импортируем файлик wiews.py со всеми представлениями (классами и методами)

from django.urls import path, include

# from .views import subscriptions

urlpatterns = [
    path('', views.NewsList.as_view(), name='news_home'),
    path('<int:pk>', views.NewsId.as_view(), name='news_id'),  # переход по динамическим страницам
    path('create/', views.NewsCreateView.as_view(), name='create'),  # переход на страницу добавления записи
    path('search/', views.SearchList.as_view(), name='search'),
    path('<int:pk>/updata', views.NewsUpdataView.as_view(), name='news_updata'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('i18n/', include('django.conf.urls.i18n')),  # подключаем встроенные эндопинты для работы с локализацией
]
