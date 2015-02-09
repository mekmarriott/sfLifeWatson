from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    url(r'^watson', views.watson, name='watson'),
    url(r'^$', views.new, name='new'),
)
