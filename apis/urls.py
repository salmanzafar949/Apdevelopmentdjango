from django.urls import path
from . import views

urlpatterns = [
    path('articles', views.ArticleListView.as_view(), name="article.index"),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name="article.detail"),
]