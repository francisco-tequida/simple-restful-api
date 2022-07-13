from django.db import models


class Brand(models.Model):
    name = models.TextField(max_length=128, unique=True)

    class Meta:
        ordering = "name",

    def __str__(self) -> str:
        return self.name
