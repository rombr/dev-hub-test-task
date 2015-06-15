# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import (
    PostCreate, SubscribeCreate, Feed, Unsubscribe, MarkPostAsRead,
)


urlpatterns = [
    url(r'^$', Feed.as_view(), name='blog-index'),
    url(r'^add/post/$', PostCreate.as_view(), name='post-add'),
    url(r'^add/subscribe/$', SubscribeCreate.as_view(), name='subscribe-add'),
    url(r'^unsubscribe/(?P<author_pk>\d+)/$', Unsubscribe.as_view(),
        name='unsubscribe'),
    url(r'^mark/post/as/read/(?P<pk>\d+)/$', MarkPostAsRead.as_view(),
        name='mark-post-as-read'),
]
