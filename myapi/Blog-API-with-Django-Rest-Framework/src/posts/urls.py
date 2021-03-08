from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url('$', post_list, name='list'),
    url('create/$', post_create),
    url('(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url('(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url('(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
