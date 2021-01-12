from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer


# 2개의 url을 생성해줌 (/post/, /post/pk/)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
