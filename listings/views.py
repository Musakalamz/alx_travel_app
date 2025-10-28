from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description="Welcome endpoint for the ALX Travel App API",
    responses={
        200: openapi.Response(
            description="Welcome message",
            examples={
                "application/json": {
                    "message": "Welcome to ALX Travel App API",
                    "version": "v1",
                    "status": "active"
                }
            }
        )
    }
)
@api_view(['GET'])
def welcome_view(request):
    """
    Welcome endpoint for the ALX Travel App API
    """
    return Response({
        "message": "Welcome to ALX Travel App API",
        "version": "v1",
        "status": "active"
    }, status=status.HTTP_200_OK)