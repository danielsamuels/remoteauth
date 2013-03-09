from django.conf.urls import patterns, url


urlpatterns = patterns('remoteauth.apps.ranks.views',
    url(r'^$', 'rank_listing', name="listing"),
    url(r'^(?P<rank>[^/]+)/$', 'rank_details', name="details"),
)

