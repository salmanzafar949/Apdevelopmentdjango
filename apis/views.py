from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializers
from rest_framework import viewsets
from rest_framework.response import Response

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


#
#
# class ArticleListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class ArticleDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class ArticleCreateView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class ArticleUpdateView(generics.UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
#
#
# class ArticleDeleteView(generics.DestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializers
