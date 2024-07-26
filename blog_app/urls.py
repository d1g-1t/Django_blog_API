from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response

from .views import (
    RegisterView, ArticleListCreateView, ArticleDetailView,
    CommentListCreateView, CommentDetailView
)


class ApiRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'register': 'api/register/',
            'articles': 'api/articles/',
            'comments': 'api/comments/',
        })


urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('register/', RegisterView.as_view(), name='api_register_create'),
    path(
        'articles/', ArticleListCreateView.as_view(),
        name='article-list-create'
    ),
    path(
        'articles/<int:pk>/', ArticleDetailView.as_view(),
        name='article-detail'
    ),
    path(
        'comments/', CommentListCreateView.as_view(),
        name='comment-list-create'
    ),
    path(
        'comments/<int:pk>/', CommentDetailView.as_view(),
        name='comment-detail'
    ),
]
