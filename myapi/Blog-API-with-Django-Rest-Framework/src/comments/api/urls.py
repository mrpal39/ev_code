from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
  

    )

urlpatterns = [
    url('', CommentListAPIView.as_view(), name='list'),
    url('create/$', CommentCreateAPIView.as_view(), name='create'),
    url('(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
