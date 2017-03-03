from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^status_list.html/$', views.status_list, name='status_list'),
    url(r'^short_status_list.html/$', views.short_status_list, name='short_status_list'),
    url(r'^(?P<status_id>\w+)/$', views.detail, name='detail'),
    url(r'^predict.html/$', views.predict, name='predict'),
    url(r'^results.html/$', views.results, name='results'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
