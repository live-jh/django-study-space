from django.conf import settings  # settings에 설정 후 지정하기
from django.db import models


# from django.contrib.auth.models import User -> 좋지 않은 유저 모델 (유저모델은 변경될수도 있기 때문)


# Create your models here.
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    post_img = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    # java의 toString과 같은 역할
    def __str__(self):
        return self.message
        # return f"Custom Post object ({self.id}-{self.message})"

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    class Meta:  # 기본 정렬
        ordering = ['-id']

    # def message_length(self): #message length 추가
    #     return len(self.message)
    # message.short_description = '메세지 글자수'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # "instagram.Post"
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name