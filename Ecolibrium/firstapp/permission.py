from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsReadOnlyOrIsAdmin(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_staff:
            return True
        allowed_methods = ['GET',]
        if request.method in allowed_methods:
            return True
        else:
            return False
