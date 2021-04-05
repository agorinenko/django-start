"""
App url patterns
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    re_path('admin/', admin.site.urls),
]
