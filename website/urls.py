from django.conf.urls import patterns, url

from website import views

urlpatterns = patterns('',
    url(r'^$', views.announcement, name='announcement'),
    url(r'announcements', views.announcement, name='announcement'),
    url(r'play', views.play, name='play'),
    url(r'about', views.about, name='about'),
    url(r'hiscores', views.hiscores, name='hiscores'),
    url(r'rules', views.rules, name='rules')
)
