from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개의 url 생성

urlpatterns = [
    path('', include(router.urls)), #url pattern list
    path('public/', views.PostListAPIView.as_view()), #url pattern list
]
