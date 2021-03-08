from django.urls import path, include
from . import views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
    
)


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product ,name='product'),


    path('blog/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delele'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),


]
