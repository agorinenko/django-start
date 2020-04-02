from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination


class MaxLimitOffsetPagination(LimitOffsetPagination):
    max_limit = settings.REST_FRAMEWORK['MAX_PAGE_SIZE']
