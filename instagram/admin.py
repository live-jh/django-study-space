from django.contrib import admin
from .models import Post


# Register your models here.
# admin.site.register(Post) #1번 방법


# class PostAdmin(admin.ModelAdmin): #2번 방법
#     pass
#
#
# admin.site.register(Post, PostAdmin)


@admin.register(Post)  # 래핑
class PostAdmin(admin.ModelAdmin):  # 3번 방법
    list_display = ['pk', 'message', 'created_at', 'updated_at']
    pass
