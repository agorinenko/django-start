from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from web_app.views.swagger_view import swagger_view

schema_view = swagger_view(title='REST API')

urlpatterns = [
    url(r'^swg(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swg/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]
