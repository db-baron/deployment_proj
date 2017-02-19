# Create a web page with blog entrys and the ability to comment underneath them
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blogs$', views.blogs),
    url(r'^comments/(?P<id>\d+)$', views.comments)  # get in comments id and pass it on to blog
]
