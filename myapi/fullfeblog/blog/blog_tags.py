
from django import template
from django.db.models import Q
from django.conf import settings
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import random
from django.urls import reverse
# from blog.models import Article, Category, Tag, Links, SideBar, LinkShowType
from django.utils.encoding import force_text
from django.shortcuts import get_object_or_404
import hashlib
import urllib
# from comments.models import Comment
from DjangoBlog.utils import cache_decorator, cache
from django.contrib.auth import get_user_model
from oauth.models import OAuthUser
from DjangoBlog.utils import get_current_site
import logging



logger = logging.getLogger(__name__)

register = template.Library()


@register.simple_tag
def timeformat(data):
    try:
        return data.strftime(settings.TIME_FORMAT)
        # print(data.strftime(settings.TIME_FORMAT))
        # return "ddd"
    except Exception as e:
        logger.error(e)
        return ""


@register.simple_tag
def datetimeformat(data):
    try:
        return data.strftime(settings.DATE_TIME_FORMAT)
    except Exception as e:
        logger.error(e)
        return ""        



@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    from DjangoBlog.utils import CommonMarkdown
    return mark_safe(CommonMarkdown.get_markdown(content))
