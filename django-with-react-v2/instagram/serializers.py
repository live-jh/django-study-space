from django.contrib.auth import get_user_model
from django.forms import forms
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Post


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
        ]


class PostSerializer(ModelSerializer):
    # author_name = serializers.ReadOnlyField(source='author.username')
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'author',
            'message',
            'created_at',
            'updated_at',
        ]

        # ModelForm과 유사
        # class PostForm(forms.ModelForm):
        #     class Meta:
        #         model = Post
        # fields = '__all__'
