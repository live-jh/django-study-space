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
