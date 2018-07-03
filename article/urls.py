from django.conf.urls import url, include
from article import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^published/$', views.ArticleListPublishedAPIView.as_view(), name='published_articles'),
    url(r'^create/$', views.ArticleCreateAPIView.as_view(), name='create_article'),
    url(r'^all/$', views.ArticleListAPIView.as_view(), name='all_articles'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.ArticleDetailAPIView.as_view(), name='article_details'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ArticleUpdateAPIView.as_view(), name='article_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ArticleDeleteAPIView.as_view(), name='article_delete'),
    url(r'^comment/create/$', views.CommentCreateAPIView.as_view(), name='comment_create'),
    url(r'^comment/update/(?P<pk>[0-9]+)/$', views.CommentUpdateAPIView.as_view(), name='comment_update'),
    url(r'^comment/delete/(?P<pk>[0-9]+)/$', views.ArticleDeleteAPIView.as_view(), name='comment_delete'),
    url(r'^comment/list/$', views.CommentListAPIView.as_view(), name='comment_list'),
    url(r'^like/create/$', views.LikeCreateAPIView.as_view(), name='like_create'),
    url(r'^like/delete/(?P<pk>[0-9]+)/$', views.LikeDeleteAPIView.as_view(), name='like_delete'),
]


