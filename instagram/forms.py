import re

from django import forms

from instagram.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'message',
            'post_img',
            'tag_set',
            'is_public',
        ]

    # form.clean_field로 접근
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message:
            message = re.sub(r'[a-zA-Z]+', '', message)  # 알파벳 공백으로 변환
        return message
