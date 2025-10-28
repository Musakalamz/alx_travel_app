from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Welcome endpoint for the ALX Travel App API",
    responses={200: openapi.Response('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING),
            'status': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ))}
)
@api_view(['GET'])
def welcome_view(request):
    """
    Welcome endpoint for the ALX Travel App API
    """
    return Response({
        'message': 'Welcome to ALX Travel App API',
        'status': 'success'
    })