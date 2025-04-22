from rest_framework.response import Response
from rest_framework.views import APIView

from web_app import models, serializers



class HelloWorldView(APIView):
    """ Получение меню"""
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'message': 'Hello, world'
        })

