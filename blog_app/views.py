from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):
    '''Регистрация нового пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_serializer = TokenObtainPairSerializer(data={
            'username': user.username,
            'password': request.data['password']
        })
        token_serializer.is_valid(raise_exception=True)
        token_data = token_serializer.validated_data

        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': serializer.data,
            'token': token_data
        }, status=status.HTTP_201_CREATED, headers=headers)


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Проверка на автора объекта'''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ArticleListCreateView(generics.ListCreateAPIView):
    '''Получение списка всех статей и создание новой статьи'''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''Получение, обновление и удаление статьи'''
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]


class CommentListCreateView(generics.ListCreateAPIView):
    '''Получение списка всех комментариев и создание нового комментария'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''Получение, обновление и удаление комментария'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
