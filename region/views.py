from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .regions import regions


class RegionList(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


# Used to add the Region from the file
# class AddRegion(APIView):
#     def get(self, request):
#         for region in regions:
#             Region.objects.create(
#                 name=region["name"], wiki_data_Id=region["wikiDataId"])
#         return Response({"message": "Success"})
