from django.urls import path
from . import views
from django.conf.urls import include, url
from django.views import generic
from material.frontend import urls as frontend_urls

urlpatterns = [
    path('', views.home, name='home'),
    path('$/', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    path('/', include(frontend_urls)),
]
    
    
# Viewflow PRO Feature Set

#     Celery integration
#     django-guardian integration
#     Flow graph visualization
#     Flow BPMN export
#     Material Frontend

#     Process dashboard view
#     Flow migration support
#     Subprocess support
#     REST API support

