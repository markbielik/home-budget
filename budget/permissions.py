from rest_framework.permissions import BasePermission


class IsTestUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.username == 'test')
