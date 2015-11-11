from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/(?P<ocassion_id>[0-9]+)$', views.ocassion, name='ocassion'),
    url(r'^/person/(?P<person_id>[0-9]+)$', views.person, name='person'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        #    'document_root': settings.MEDIA_ROOT,
        #}),
        #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        url(r'^(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
