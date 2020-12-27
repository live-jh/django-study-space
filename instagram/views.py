from warnings import catch_warnings

from django.shortcuts import render
from .models import Post, Comment


# Create your views here.

def post_list(request):
    post_set = Post.objects.all()
    q = request.GET.get('q', '')

    if q:
        post_set = post_set.filter(message__icontains=q)

    return render(request, 'instagram/post_list.html', {
        'post_list': post_set,
        'q': q,
    })
