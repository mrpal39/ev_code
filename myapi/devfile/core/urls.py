from django.urls import path,include
from core  import views


urlpatterns = [
    path('', views.base, name='base'),

    path('home/', views.home, name='home'),
    path('search/', views.Search, name='home_search'),

    # path('', views.home, name='home'),
    ]
