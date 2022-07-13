from django.contrib import admin
from django.urls import path
from swagger_documentation.documentation import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger"),
    path('admin/', admin.site.urls),
]
