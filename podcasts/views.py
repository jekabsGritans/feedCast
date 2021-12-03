from django.shortcuts import render
from .models import Podcast


def podcast_list(request):
    podcasts = Podcast.objects.all().order_by('date_created') #filter by current user
    return render(request, 'podcasts/podcast_list.html', {'podcasts': podcasts})


def podcast_detail(request, slug):
    podcast = Podcast.objects.get(slug=slug)
    episodes = podcast.episode_set.all().order_by('date_published')
    return render(request, 'podcasts/podcast_detail.html', {'podcast': podcast, 'episodes': episodes})


def edit_podcast(request, slug):
    podcast = Podcast.objects.get(slug=slug)
    return render(request, 'podcasts/podcast_edit.html', {'podcast': podcast})

