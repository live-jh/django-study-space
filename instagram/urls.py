from django.urls import path, re_path, register_converter
from django.views.generic import TemplateView

from . import views
from .common.converters import YearConverter, MonthConverter, DayConverter

app_name = 'instagram' #URL Reverse에서 namespace역할

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')



urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),

    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),  # re_path 정규표현식 위와 같다
    # path('archives/<year:year>', views.archives_year),  # 좌 year는 컨버터명 우 year는 view의 매개변수명
    path('archive', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/', views.post_archive_month, name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/', views.post_archive_day, name='post_archive_day'),
]
