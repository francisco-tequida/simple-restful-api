from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        fields = (
            "username",
            "password",
            "email",
            "is_staff"
        )

        extra_kwargs = {
            "email": {"required": True},
            "is_staff": {"required": True},
            "password": {"write_only": True}
        }
