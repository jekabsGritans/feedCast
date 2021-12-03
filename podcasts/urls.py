from django.urls import path, include
from . import views
from .feeds import PodcastFeed

app_name = 'podcasts'

urlpatterns = [
    path('', views.podcast_list, name='list'),
    path('<slug:slug>',views.podcast_detail, name='detail'),
    path('<slug:slug>/edit/', views.edit_podcast, name='edit'),
    path('<slug:slug>/episode/',include('episodes.urls','episodes')),
    path('<slug:slug>/rss/',PodcastFeed())
]

