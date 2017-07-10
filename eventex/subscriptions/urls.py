from django.conf.urls import url
# from django.contrib import admin
# from eventex.core.views import home
from eventex.subscriptions.views import new, detail
urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
]
