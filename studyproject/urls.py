"""studyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # from 프로젝트명 import settings + django.conf import global_settings 의 합친 역할
from django.views.generic import TemplateView, RedirectView

api_v1_patterns = [

]

# TemplateView 다른 사용법
# class RootView(TemplateView):
#     template_name = 'root.html'


urlpatterns = [
    # path('api/v1/', include(api_v1_patterns)),
    # path('', include('blog1.urls')),
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),  # TemplateView, or RootView.as_view()
    path('', RedirectView.as_view(pattern_name="instagram:post_list"), name='root'),  # RedirectView (redirect시킬 url지정가능하며, pattern_name="앱이름:앱의path명") instagram:post_list
    path('admin/', admin.site.urls),  # URL Reverse (path를 변경해도 알아서 장고에서 매핑됌)
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]

# debug toolbar 추가
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
# settings.MEDIA_URL
# settings.MEDIA_ROOT
