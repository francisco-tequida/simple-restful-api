from rest_framework import permissions
from rest_framework.request import Request


SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]

class ProductPermission(permissions.BasePermission):
    """ Class to allow the user to perform queries freely to the SAFE METHODS
    but require a valid token when querying the other methods.
    """
    def has_permission(self, request: Request, view) -> bool:
        if (request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff):
            return True
        return False
