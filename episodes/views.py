from django.shortcuts import render
from .models import Episode
from podcasts.models import Podcast


def episode_detail(request, slug, ep_slug):
    podcast = Podcast.objects.get(slug=slug)
    episode = podcast.episode_set.get(slug=ep_slug)
    return render(request, 'episodes/episode_detail.html', {'podcast': podcast, 'episode': episode})


def edit_episode(request, slug, ep_slug):
    podcast = Podcast.objects.get(slug=slug)
    episode = podcast.episode_set.get(slug=ep_slug)
    if request.method == 'POST':
        #do stuff
        pass

    episode = Episode.objects.get(slug=slug)
    return render(request, 'episodes/episode_edit.html', {'episode': episode})
