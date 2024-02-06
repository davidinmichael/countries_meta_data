from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.staticfiles import finders
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from .countries import countries
from .places import places

class CreateCurrency(APIView):
    def get(self, request):
        for place in places:
            try:
                currency_instance = Currency.objects.get(name=place["currency_name"])
            except Currency.DoesNotExist:
                currency = Currency.objects.create(name=place["currency_name"], currency_symbol=place["currency_symbol"], currency=place["currency"])
        return Response({"message": "All currency created"})


class CreateCountry(APIView):
    def get(self, request):
        for place in places:

            currency = Currency.objects.get(name=place["currency_name"])
            try:
                Country.objects.get(name=place["name"])
            except Country.DoesNotExist:
                country = Country.objects.create(name=place["name"],
                capital=place["capital"],
                phone_code=place["phone_code"],
                currency=currency,
                iso2=place["iso2"],
                iso3=place["iso3"],
                latitude=place["latitude"],
                longitude=place["longitude"])
        return Response({"message": "All Countries created"})
    

class CreateState(APIView):
    def get(self, request):
        for place in places:
            country = Country.objects.get(name=place["name"])
            for state in place["states"]:
                try:
                    State.objects.get(name=state["name"])
                except State.DoesNotExist:
                    states = State.objects.create(name=state["name"],
                    state_code=state["state_code"],
                    country=country,
                    latitude=state["latitude"],
                    longitude=state["longitude"],
                    identifier=state["id"])
        return Response({"message": "All States created"})


class CreateCity(APIView):
    def get(self, request):
        for place in places:
            for state in place["states"]:
                state_instance = State.objects.get(name=state["name"])
                for city in state["cities"]:
                    try:
                        City.objects.get(name=city["name"])
                    except City.DoesNotExist:
                        city_instance = City.objects.create(name=city["name"], state=state_instance,
                        latitude=city["latitude"], longitude=city["longitude"])
        return Response({"message": "All Cities created"})

class AllCountries(APIView, PageNumberPagination):
    def get(self, request):
        all_countries = Country.objects.all()
        response = self.paginate_queryset(all_countries, request, view=self)
        serializer = CountrySerializer(response, many=True)
        return self.get_paginated_response(serializer.data)

