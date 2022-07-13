from rest_framework import viewsets
from rest_framework.response import Response
from products.models import Product, ProductTrack
from products.serializers import ProductSerializer
from permissions.product_permissions import ProductPermission


class ProductModelViewSet(viewsets.ModelViewSet):
    """Class to handle queries related to the product model"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    lookup_field = "slug"


    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method to update the amount of times a single
        item is requested.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if request.user is None:
            ProductTrack.objects.create(product=instance)
        elif request.user.is_staff is False:
            ProductTrack.objects.create(product=instance, user=request.user)

        return Response(serializer.data)