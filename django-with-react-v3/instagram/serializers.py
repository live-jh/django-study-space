from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_email = serializers.ReadOnlyField(source='author.email')

    # field level 검사 (유효성 검사 및 값 반환)
    # def validate_name(self, value):
    #     if 'study' not in value:
    #         raise ValidationError("닉네임에 study가 포함되어야 합니다.")
    #     return value

    # object level 검사 (유효성 검사 및 값 반환)
    # def validate(self, data):
    #     if 'study' not in data['author_name']:
    #         raise ValidationError("닉네임에 study가 포함되어야 합니다.")
    #     return data

    class Meta:
        model = Post
        fields = [
            'id',
            'author_name',
            'author_email',
            'message',
            'created_at',
            'updated_at',
            'is_public',
            'ip',
        ]
