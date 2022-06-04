from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('services/scraper', views.scraper, name='scraper'),
    path('services/analytics', views.analytics, name='analytics'),
    path('download', views.download, name='download'),
]
