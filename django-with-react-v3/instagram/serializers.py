from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_email = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Post
        fields = [
            'id',
            'author_name',
            'author_email',
            'message',
            'created_at',
            'updated_at',
            'is_public'
        ]
