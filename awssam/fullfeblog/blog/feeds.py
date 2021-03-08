from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post



class LatestPostsFeed(Feed):
    title ='My Blog'
    link=reverse_lazy('post_list')
    description = 'new post of my Blog.'
    

    def  items(self):
        return Post.published.all()[:5]

    def  item_title(self, item):
        return super().item_title(item)    


    def item_description(self, item):
        return truncatewords(item.body,30)     
