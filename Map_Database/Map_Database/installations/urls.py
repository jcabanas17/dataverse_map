from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dataverse/(?P<institution_name>\S*)/$', views.installations, name='newinstitution'),
    url(r'^$', views.index, name='installations_index'),
    url(r'^$', views.institutions, name='institution_index'),
] 
