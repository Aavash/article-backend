from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from article import views

router = DefaultRouter()

# router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^published/$', views.ArticleListPublishedAPIView.as_view(), name='published_articles'),
    url(r'^create/$', views.ArticleCreateAPIView.as_view(), name='create_article'),
    url(r'^all/$', views.ArticleListAPIView.as_view(), name='all_articles'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.ArticleDetailAPIView.as_view(), name='article_details'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.ArticleUpdateAPIView.as_view(), name='article_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.ArticleDeleteAPIView.as_view(), name='article_delete'),
]


urlpatterns = format_suffix_patterns(urlpatterns)

