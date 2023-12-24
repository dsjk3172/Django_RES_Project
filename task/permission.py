from rest_framework import permissions


class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.create_user == request.user
    
# 권한
# Task 조회: All
# Task 생성: 로그인 사용자
# Task 수정 및 삭제: 글 작성자