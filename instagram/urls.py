from django.urls import path, re_path, register_converter
from django.views.generic import TemplateView

from . import views

app_name = 'instagram' #URL Reverse에서 namespace역할

class YearConverter:
    regex = r"20\d{2}"

    # url 매칭 후 view 함수 호출전 인자 검사
    def to_python(self, value):
        return int(value)

    # url reverse
    def to_url(self, value):
        # return "%04d" % value
        return str(value)


register_converter(YearConverter, 'year')


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),  # re_path 정규표현식 위와 같다
    path('archives/<year:year>', views.archives_year),  # 좌 year는 컨버터명 우 year는 view의 매개변수명
]
