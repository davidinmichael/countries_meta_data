from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.staticfiles import finders
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from .countries import countries


class AllCountries(APIView, PageNumberPagination):
    def get(self, request):
        all_countries = Country.objects.all()
        response = self.paginate_queryset(all_countries, request, view=self)
        serializer = CountrySerializer(response, many=True)
        data = self.get_paginated_response(serializer.data)
        return Response(data, status.HTTP_200_OK)


class AddCountries(APIView):
    def get(self, request):
        for country in countries:
            if country["capital"]:
                Country.objects.create(
                    name=country["name"], capital=country["capital"],
                    region=country["region"], iso2=country["iso2"],
                    iso3=country["iso3"], numeric_code=country["numeric_code"],
                    phone_code=country["phone_code"], currency=country["currency"],
                    currency_name=country["currency_name"])
        return Response({"message": "All Countries Added"}, status.HTTP_201)
