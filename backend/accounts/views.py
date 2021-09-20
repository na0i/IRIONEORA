from django.shortcuts import render
from drf_yasg.openapi import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def test(request):
    return Response(request)