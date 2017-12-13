from .views import home,link
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^$', home, name = "home"),
    #url(r'^list/$', LinkList.as_view(), name = "create"),
    #url(r'^(?P<pk>[\w-]+)/$', LinkDetail.as_view(), name = "retrieve"),
    #url(r'^list/$', LinkList.as_view(), name = "create"),
    url(r'^(?P<ids>[\w-]+)/$', link),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()