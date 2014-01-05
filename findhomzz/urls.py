from django.conf.urls import patterns, include, url
from findhomzz.views import index

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('', url(r'^$', index),)
