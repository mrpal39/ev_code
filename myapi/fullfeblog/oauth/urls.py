
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = "oauth"
urlpatterns = [
    path(
        'oauth/authorize',
        views.authorize),
    path(
        'oauth/requireemail/<int:oauthid>.html',
        views.RequireEmailView.as_view(),
        name='require_email'),
    path(
        'oauth/emailconfirm/<int:id>/<sign>.html',
        views.emailconfirm,
        name='email_confirm'),
    path(
        'oauth/bindsuccess/<int:oauthid>.html',
        views.bindsuccess,
        name='bindsuccess'),
    path(
        'oauth/oauthlogin',
        views.oauthlogin,
        name='oauthlogin')]