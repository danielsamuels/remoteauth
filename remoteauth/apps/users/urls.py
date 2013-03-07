from django.conf.urls import patterns, include, url
from .views import UserView


urlpatterns = patterns('',
    url(r'(?P<user>[^/]+)/$', UserView.as_view(), name="view"),
)

