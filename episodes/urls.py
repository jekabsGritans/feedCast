from django.urls import path
from . import views

app_name = 'episodes'

urlpatterns = [
    path('<slug:ep_slug>', views.episode_detail, name='detail'),
    path('<slug:ep_slug>/edit/', views.edit_episode, name='edit'),
]