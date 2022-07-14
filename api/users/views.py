from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    """Class to handle queries related to user model"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def create(self, request: Request, *_) -> Response:
        """
        Create method override.
        This override set a hasshed password to the user instance when POST
        method is called.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        instance.set_password(request.data.get("password"))
        instance.save()
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request: Request, *args, **kwargs) -> Response:
        """
        Update method override.
        This override set a hasshed password to the user instance when PUT
        method is called.
        """
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(request.data.get("password"))
        instance.save()

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
