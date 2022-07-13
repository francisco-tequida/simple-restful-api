from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from swagger_documentation.documentation import schema_view
from users.views import UserModelViewSet
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r"api/users", UserModelViewSet, "users")

urlpatterns = [
    path(
        "swagger/",
        schema_view.with_ui('swagger', cache_timeout=0),
        name="swagger"
    ),
    path("", include(router.urls)),
    path(
        "api/token/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path('admin/', admin.site.urls),
]
