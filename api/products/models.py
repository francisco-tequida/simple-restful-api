import typing
from django.db import models
from django.utils.text import slugify
from brands.models import Brand


class Product(models.Model):
    sku = models.TextField(max_length=64, unique=True)
    name = models.TextField(max_length=128, unique=True)
    price = models.DecimalField(max_digits=15, decimal_places=5)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("name", "sku")

    def __str__(self) -> str:
        return f"{self.sku} - {self.name}"

    def save(self, *args, **kwargs) -> None:
        """Override save method to generete a valid slug"""
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
