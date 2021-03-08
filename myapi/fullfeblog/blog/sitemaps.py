from django.contrib.sitemaps import Sitemap
from  . models import Post



class PostSitemap(Sitemap):
    changefreq='weekly'  # You create a custom sitemap by inheriting the Sitemap class of the sitemaps
    priority = 0.9       # module. The changefreq and priority attributes indicate the change frequency
      # of your post pages and their relevance in your website (the maximum value is 1 ).


    def items(self):
        return Post.published.all()


    def lastmod(self,obj):
        return obj.updated    
    
