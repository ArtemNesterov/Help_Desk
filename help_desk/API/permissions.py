from rest_framework import permissions


class IsSuperUser(permissions.IsAdminUser):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            if request.method == 'DELETE':
                return False
            if request.method == 'PATCH':
                return True


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

    def has_permission(self, request, view):
        return True
