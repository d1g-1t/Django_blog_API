from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article, Comment


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели User'''

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ArticleSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Article'''
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'author', 'created_at', 'updated_at'
        ]


class CommentSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Comment'''
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id', 'article', 'content', 'author', 'created_at', 'updated_at'
        ]
