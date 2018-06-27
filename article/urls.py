from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from article import views

router = DefaultRouter()

router.register(r'snippets', views.SnippetViewSet)


