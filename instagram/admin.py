from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# Register your models here.
# admin.site.register(Post) #1번 방법


# class PostAdmin(admin.ModelAdmin): #2번 방법
#     pass
#
#
# admin.site.register(Post, PostAdmin)


@admin.register(Post)  # 래핑
class PostAdmin(admin.ModelAdmin):  # 3번 방법
    list_display = ['pk', 'img_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']  # 다른 필드에 a tag 링크를 잡고 싶을떄
    search_fields = ['message']  # 검색 input 추가
    list_filter = ['created_at', 'is_public']

    def img_tag(self, post):
        if post.post_img:
            return mark_safe(f'<img style="width:75px;" src="{post.post_img.url}"/>')
        return None

    # admin에서도 함수 구현 가능
    def message_length(self, post):
        return f"{len(post.message)} 글자 입니다."


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
