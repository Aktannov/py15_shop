from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff

    # UPDATE, DELETE, RETRIEVE
    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff

class IsAuthor(BasePermission): #евляется ли он автором коммента
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user == obj.author