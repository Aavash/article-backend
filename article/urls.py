from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from article import views

router = DefaultRouter()

# router.register(r'snippets', views.SnippetViewSet)

urlpatterns = [
    url(r'^all_articles/$', views.ArticleListAPIView),
    url(r'^published_articles/$', views.ArticleListPublishedAPIView),
    url(r'^article_details/(?P<pk>[0-9]+)/$', views.APIView),
]


urlpatterns = format_suffix_patterns(urlpatterns)

