
from django.conf import settings
# from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token

from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('comments/', include("comments.urls", namespace='comments')),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include("posts.urls", namespace='posts')),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include("accounts.api.urls", namespace='users-api')),
    path('api/comments/', include("comments.api.urls", namespace='comments-api')),
    path('api/posts/', include("posts.api.urls", namespace='posts-api')),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)