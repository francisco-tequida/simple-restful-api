from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, ProductTrack
from products.serializers import ProductSerializer
from permissions.product_permissions import ProductPermission
from django.forms.models import model_to_dict
from utils.products_utils import send_product_information_updated_email


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

    def update(self, request, *args, **kwargs):
        """Override update method to send an email everytime a product info is
        updated"""
        partial = kwargs.pop('partial', False)

        instance = self.get_object()
        prev_data = model_to_dict(instance)
        curr_data = request.data

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        try:
            send_product_information_updated_email(prev_data, curr_data)
        except Exception:
            return Response({
                "message": "SendGrid exception, are all SendGrid env variables set properly?"
            },status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
