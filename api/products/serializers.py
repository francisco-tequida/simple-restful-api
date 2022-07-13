from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

        extra_kwargs = {
            "slug": {"read_only": True}
        }
