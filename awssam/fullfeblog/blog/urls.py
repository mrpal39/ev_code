from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView
)
from . import views

from .feeds import  LatestPostsFeed

urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('blog/', views.post_list, name='post_list'),
    path('<int:year>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path('tag/<slug:tag_slug>/',
        views.post_list, name='post_list_by_tag'),     
]
