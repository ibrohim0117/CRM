from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class IsAuthenticatedOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        # Agar so'rov turi Post bo'lsa, har qanday foydalanuvchiga ruxsat beriladi
        if request.method == 'POST':
            return True
        # Aks holda, foydalanuvchi faqatgina login bo'lsa ruxsat beriladi
        return request.user and request.user.is_authenticated


class IsOwnerOrSuperuserOrAuthenticatedOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        user = request.user
        return user.id == obj.id or user.is_superuser


class IsClintOwnerAuthenticatedOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        clint = obj.customer.id
        owner = request.user.id
        return (clint == owner or request.user.is_superuser) and request.user.is_authenticated

