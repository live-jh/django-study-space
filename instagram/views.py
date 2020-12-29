from warnings import catch_warnings

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment


# Create your views here.

post_list = ListView.as_view(model=Post) #ListView 활용 (search 불가)
#or
#class PostListView(ListView):
#   model = Post
#post_list = PostListView.as_view()

# def post_list(request):
#     post_set = Post.objects.all()
#     q = request.GET.get('q', '')
#
#     if q:
#         post_set = post_set.filter(message__icontains=q)
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': post_set,
#         'q': q,
#     })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    #request.method
    #request.META, request.GET, Post, body, FILES등
    return render(request, 'instagram/post_list.html')
