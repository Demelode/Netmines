from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'main', views.main, name='main'),
    url(r'play', views.play, name='play'),
    url(r'about', views.about, name='about'),
    url(r'hiscores', views.hiscores, name='hiscores'),
)
