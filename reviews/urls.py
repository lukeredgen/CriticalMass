from django.conf.urls import url, patterns, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', 'reviews.views.all_reviews'),
    url(r'^(?P<review_id>\d+)/$', 'reviews.views.review'),

    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api/albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    url(r'^api/albums/$', views.AlbumReviews.as_view()),
    url(r'^api/games/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
    url(r'^api/tv/series/(?P<pk>[0-9]+)/$', views.TVSeriesDetail.as_view()),
    url(r'^api/movies/(?P<pk>[0-9]+)/$', views.MovieDetail.as_view()),
    url(r'^api/books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^api/tracks/(?P<pk>[0-9]+)/$', views.TrackDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)