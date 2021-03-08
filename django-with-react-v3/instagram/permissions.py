from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):
    # 인증되어야 조회, 등록 허용
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # 작성자만 수정
        return obj.author == request.user
