from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAuthenticatedOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        # Agar so'rov turi Post bo'lsa, har qanday foydalanuvchiga ruxsat beriladi
        if request.method == 'POST':
            return True
        # Aks holda, foydalanuvchi faqatgina login bo'lsa ruxsat beriladi
        return request.user and request.user.is_authenticated

