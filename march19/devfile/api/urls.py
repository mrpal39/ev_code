from django.conf.urls import url
from . import views

urlpatterns = [
    url('api/', views.apiurl, name='index'),

]