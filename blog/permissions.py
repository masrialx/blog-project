from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow full access to admins and owners
        return request.user.is_staff or obj.author == request.user

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access only to admins
        return request.user.is_staff
