from django.forms import forms
from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# ModelForm과 유사
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
        fields = '__all__'


