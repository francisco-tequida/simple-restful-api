from rest_framework import viewsets
from products.models import Product
from products.serializers import ProductSerializer
from permissions.product_permissions import ProductPermission


class ProductModelViewSet(viewsets.ModelViewSet):
    """Class to handle queries related to the product model"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    lookup_field = "slug"
