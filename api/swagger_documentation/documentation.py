from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Simple API",
        default_version='0.1.0',
        description="API documentation",
    ),
    public=True,
)
