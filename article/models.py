from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publisher', null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField(default=False)


class Like(models.Model):
    liked_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='liked_article', null=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user', null=True)
    like = models.BooleanField(default=False)


class Comment(models.Model):
    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='commented_article',
                                          null=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commented_user', null=True)
    comment = models.CharField(max_length=255)
    commented_date = models.DateTimeField(auto_now_add=True)