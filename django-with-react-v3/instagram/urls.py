from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
# from .views import PublicPostListAPIView

router = DefaultRouter()
router.register('post', views.PostViewSet)  # 2개의 URL 생성, 첫번째 인자는 http 요청시 prefix로 지정하는 것 등록 ex: 'post/'

urlpatterns = [
    path('', include(router.urls)),
    # path('public/', PublicPostListAPIView.as_view(), name="post_list")
]
