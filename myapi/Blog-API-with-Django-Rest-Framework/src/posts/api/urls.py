from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostCreateAPIView,
    PostDeleteAPIView,
    PostDetailAPIView,
    PostListAPIView,
    PostUpdateAPIView,
    )

urlpatterns = [
    url('$', PostListAPIView.as_view(), name='list'),
    url('create/$', PostCreateAPIView.as_view(), name='create'),
    url('(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url('(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url('(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
]
