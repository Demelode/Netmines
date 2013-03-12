from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from website.views import UserList, UserDetail, GroupList, GroupDetail, GameList, GameDetail

from website import views

urlpatterns = patterns('website.views',
    url(r'^$', views.main, name='main'),
    url(r'main', views.main, name='main'),
    url(r'play', views.play, name='play'),
    url(r'about', views.about, name='about'),
    url(r'hiscores', views.hiscores, name='hiscores'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
    url(r'^game/$', GameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>\d+)/$', GameDetail.as_view(), name='game-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
