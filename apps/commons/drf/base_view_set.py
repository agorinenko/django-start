from abc import ABC

from django.db.models import ProtectedError
from drf_toolkit.decorators import except_error
from drf_toolkit.errors import DjangoModelError, ApiViewError
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied


class BaseViewSet(viewsets.ModelViewSet, ABC):
    """
    DRF BaseViewSet
    """
