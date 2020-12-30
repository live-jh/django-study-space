from . import views
from django.urls import path, include

app_name = 'blog1' #URL Reverse에서 namespace역할

urlpatterns = [
    path('', views.post_list, name='post_list'),
]