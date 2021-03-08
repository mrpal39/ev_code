from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown
from django.db.models import Count
register = template.Library()


@register.filter(name='markdown')
def markdown_fromat(text):
    return mark_safe(markdown.markdown(text))

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts} 



@register.simple_tag
# In the preceding template tag, you build a QuerySet using the annotate() function
# to aggregate the total number of comments for each post. You use the Count
# aggregation function to store the number of comments in the computed field total_
# comments for each Post object. You order the QuerySet by the computed field in
# descending order. You also provide an optional count variable to limit the total
def get_most_commented_posts(count=2):
    return Post.published.annotate(
        total_comments=Count('comments')
        ).order_by('-total_comments')[:count]