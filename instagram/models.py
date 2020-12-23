from django.db import models


# Create your models here.
class Post(models.Model):
    message = models.TextField()
    post_img = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # java의 toString과 같은 역할
    def __str__(self):
        # return f"Custom Post object ({self.id}-{self.message})"
        return self.message

    class Meta: # 기본 정렬 
        ordering = ['-id']
    # def message_length(self): #message length 추가
    #     return len(self.message)
    # message.short_description = '메세지 글자수'
