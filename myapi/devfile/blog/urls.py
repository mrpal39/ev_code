from django.urls import path,include
from blog  import views


urlpatterns = [
    # path('', views.index, name='base'),
    path('', views.list, name='list'),

    # path('home/', views.home, name='home'),
    # path('search/', views.Search, name='home_search'),

    # path('', views.home, name='home'),
    ]
