from article.permissions import IsOwnerOrReadOnly
from models import Article, Like, Comment
from rest_framework import mixins

from serializers import ArticleSerializer, UserSerializer, LikeSerializer, CommentSerializer
from rest_framework import generics
from rest_framework import permissions


class ArticleListPublishedAPIView(generics.ListAPIView):
    model = Article
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer


class ArticleListAPIView(generics.ListAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(generics.RetrieveAPIView):
    model = Article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreateAPIView(generics.CreateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ArticleSerializer


class ArticleUpdateAPIView(generics.UpdateAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = ArticleSerializer


class ArticleDeleteAPIView(generics.DestroyAPIView):
    model = Article
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = ArticleSerializer


class LikeCreateAPIView(generics.CreateAPIView):
    model = Like
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = LikeSerializer


class LikeDeleteAPIView(generics.DestroyAPIView):
    model = Like
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    serializer_class = LikeSerializer


# class CommentListAPIView(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer


class CommentUpdateAPIView(generics.UpdateAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer


class CommentDeleteAPIView(generics.DestroyAPIView):
    model = Comment
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAdminUser, IsOwnerOrReadOnly,)
    serializer_class = CommentSerializer

# from django.http import Http404
#
# from models import Article, Like, Comment
# from serializers import ArticleSerializer, UserSerializer, LikeSerializer, CommentSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class ArticleListPublishedAPIView(APIView):
#     """
#     List all the published api
#     """
#     def get(self, request, format=None):
#         articles = Article.objects.filter(published= True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#
# class ArticleListAPIView(APIView):
#     """"
#     List all the articles or create a new article
#     """
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ArticleDetailAPIView(APIView):
#     """
#     Retrieve, update or delete a article instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)