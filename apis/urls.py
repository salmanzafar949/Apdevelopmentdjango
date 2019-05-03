# from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet, basename='article')
urlpatterns = router.urls

#
# urlpatterns = [
#     path('articles', views.ArticleListView.as_view(), name="article.index"),
#     path('article/store', views.ArticleCreateView.as_view(), name="article.store"),
#     path('article/<int:pk>', views.ArticleDetailView.as_view(), name="article.detail"),
#     path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name="article.update"),
#     path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name="article.delete"),
# ]