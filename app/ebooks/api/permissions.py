from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        """ admin clients can change database but other clients can view """
        is_admin = super().has_permission(request, view)
        # print("REQUEST", request.method)
        # print("SAFE METHODS",  permissions.SAFE_METHODS)
        return request.method in permissions.SAFE_METHODS or is_admin
