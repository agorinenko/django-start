from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


def swagger_view(title=None, default_version='v1'):
    schema_view = get_schema_view(
        openapi.Info(
            title=title,
            default_version=default_version,
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    return schema_view
