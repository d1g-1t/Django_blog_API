from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Документация API для приложения Blog",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@blog.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(TokenAuthentication,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog_app.urls')),
    path(
        'api/token/', TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/', TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'swagger/', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]