from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.staticfiles import find
from .models import *
from .serializers import *
import json


class RegionList(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request):
        pass
