from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics


class PostListAPIView(generics.ListCreateAPIView):  # Public -> objects.filter(is_public=True)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 2개의 url을 생성해줌 (/post/, /post/pk/)
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print('request.body -> ', request.body)
        print('request.POST -> ', request.POST)
        return super().dispatch(request, *args, **kwargs)
