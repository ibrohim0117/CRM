from rest_framework.permissions import BasePermission


class IsOrderOwnerAuthenticatedOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        # print(obj.client.customer)
        # print(obj.client)
        # print(request.user)
        return (obj.client.customer == request.user or request.user.is_superuser) and request.user.is_authenticated