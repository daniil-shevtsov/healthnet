from django.conf.urls import  include, url

from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'prototype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    re_path(r'^', include('healthnet.urls', namespace="healthnet")),
    re_path(r'^admin/', admin.site.urls),
]
