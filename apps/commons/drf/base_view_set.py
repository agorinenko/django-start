from abc import ABC
from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet, ABC):
    """
    DRF BaseViewSet
    """
