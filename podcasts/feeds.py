from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Podcast

class PodcastFeedType(Rss201rev2Feed):
        def rss_attributes(self):
            attrs = super().rss_attributes()
            attrs['xmlns:media'] = 'https://search.yahoo.com/mrss/'
            attrs['xmlns:itunes'] = 'https://www.itunes.com/dtds/podcast-1.0.dtd'
            attrs['xmlns:dcterms'] = 'https://purl.org/dc/terms/'
            attrs['xmlns:spotify'] = 'https://www.spotify.com/ns/rss'
            attrs['xmlns:psc'] = 'https://podclove.org/simple-chapters/'
            return attrs

        def add_root_elements(self, handler):
            handler.addQuickElement('title', self.feed['title'])
            handler.addQuickElement('language', self.feed['language'])
            handler.addQuickElement('description', self.feed['description'])
            handler.addQuickElement('link', self.feed['link']) 
            handler.addQuickElement('itunes:author', self.feed['itunes_author'])
            handler.addQuickElement('itunes:image', self.feed['itunes_image']) # specify default image url

            if not self.feed['itunes_explicit']:
                explicit='clean'
            else: explicit='yes'
            handler.addQuickElement('itunes:explicit', explicit)

            handler.startElement('itunes:category', {'text':self.feed['itunes_category']})
            for subcat in self.feed['itunes_subcategories']:
                handler.addQuickElement('itunes:category', contents = None, attrs = {'text':subcat})
            handler.endElement('itunes:category')

            if not self.feed['itunes_complete']:
                complete = 'no'
            else: complete = 'yes'
            handler.addQuickElement('itunes:complete', complete)

            handler.addQuickElement('itunes:type', self.feed['itunes_type'])
            handler.addQuickElement('spotify:limit', self.feed['spotify_limit'])#not as in spec
            handler.addQuickElement('spotify:countryOfOrigin', " ".join([self.feed['spotify_countryOfOrigin']]))#supply a list




class PodcastFeed(Feed):

    feed_type=PodcastFeedType

    def get_object(self, request, slug):
        return Podcast.objects.get(slug=slug)

    def title(self, pod):
        return pod.title

    def description(self, pod):
        return pod.description

    def language(self, pod):
        return pod.language.text

    def link(self, pod):
        return "/rss/"+pod.slug
    
    def itunes_author(self, pod):
        return "Jekabs"
    
    def itunes_image(self, pod):
        return "/default.jpg"

    def itunes_explicit(self, pod):
        return pod.itunes_explicit
    
    def itunes_category(self, pod):#fix (also model)
        return "arts"
    
    def itunes_subcategories(self, pod):
        return ['modern','renisance']
    
    def itunes_complete(self, pod):
        return False
    
    def itunes_type(self, pod):
        return pod.itunes_type
    
    def spotify_limit(self, pod):
        return pod.spotify_limit
    
    def spotify_countryOfOrigin(self, pod):#fix (also model)
        return ['lv','lt']
    
    


    def items(self, pod):
        return pod.episode_set.all().order_by('date_published')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return "https://test.com/124"
    
    ADDED_FIELDS=(
        "itunes_author", "itunes_image", "itunes_explicit", "itunes_category", "itunes_subcategories", "itunes_complete", "itunes_type", "spotify_limit", "spotify_countryOfOrigin" 
    )
    def feed_extra_kwargs(self, obj):
        kwargs = {}
        for field in self.ADDED_FIELDS:
            if (val := self._get_dynamic_attr(field, obj)): kwargs[field] = val
        return kwargs 
