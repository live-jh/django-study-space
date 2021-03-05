from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from .models import Post


# 밑에 2개의 처리를 이 하나의 코드로 대체
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# def post_list(request):
#     pass
#
#
# def post_detail(request, id):
#     pass
