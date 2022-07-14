from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from brands.models import Brand
from brands.serializers import BrandSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    """Class to handle queries related to brand model"""
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminUser]
