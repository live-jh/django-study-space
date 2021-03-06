from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer
from .models import Post


# generics를 이용한 View
# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

# Class를 이용한 View
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         post = Post.objects.filter(is_public=True)
#         post = PostSerializer(post, many=True).data
#         return Response(post, status=200)


# 함수를 이용한 View
# @api_view(['GET'])
# def public_post_list(request):
#     post = Post.objects.filter(is_public=True)
#     post = PostSerializer(post, many=True).data
#     return Response(post, status=200)


# 밑에 2개의 처리를 이 하나의 코드로 대체
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # ViewSet에 새로운 EndPoint
    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.queryset.filter(is_public=True)
        data_set = self.get_serializer(qs, many=True).data
        return Response(data_set)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        data = self.get_serializer(instance).data
        return Response(data)

    # def list(self, request, *args, **kwargs):
    #     pass
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):
    #     pass

    def dispatch(self, request, *args, **kwargs):
        print(request.body)  # logger
        print(request.POST)  # logger
        return super().dispatch(request, *args, **kwargs)

# @csrf_exempt  # 장식자
# def post_list(request):
#     pass#

# def post_list(request):
#     pass
#
# post_list = csrf_exempt(post_list)

# def post_detail(request, id):
#     pass
