from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^/watsonresponse', views.handle_watson, name='watson'),
	url(r'^/watson', views.watson, name='watson'),
    url(r'^$', views.new, name='new'),
]