from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^update', views.update),
    url(r'^logout', views.logout),
    url(r'^home', views.home),
    url(r'^login', views.login),
    url(r'^admin/(?P<num>\d+)$', views.show),
    url(r'^admin/(?P<num>\d+)/destroy$', views.destroy),
    url(r'^create$', views.create),
    url(r'^admin', views.admin),
    url(r'^', views.index),
]
