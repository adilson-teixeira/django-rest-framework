from rest_framework import permissions

class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        """Apenas superusuário tem permissão para exclusão"""
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True