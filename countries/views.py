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
from .regions import regions


# Used to add the Region from the file
class CreateRegion(APIView):
    def get(self, request):
        for region in regions:
            try:
                new_region = Region.objectts.get(name=region['name'])
            except Region.DoesNotExist:
                new_region = Region.objects.create(
                    name=region["name"], wiki_data_Id=region["wikiDataId"])
        return Response({"message": "Success"})
    
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
            region = Region.objects.get(name=place["region"])
            currency = Currency.objects.get(name=place["currency_name"])
            try:
                Country.objects.get(name=place["name"])
            except Country.DoesNotExist:
                country = Country.objects.create(name=place["name"],
                capital=place["capital"],
                region=region,
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



class RegionList(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class CurrencyView(APIView):
    def get(self, request):
        """Returns all currencies available in our database."""
        currency = Currency.objects.all()
        serializer = CurrencySerializer(currency, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
        
class CountryView(APIView, PageNumberPagination):
    def get(self, request):
        all_countries = Country.objects.all()
        response = self.paginate_queryset(all_countries, request, view=self)
        serializer = CountrySerializer(response, many=True)
        return self.get_paginated_response(serializer.data)


class StateView(APIView):
    def get(self, request):
        """Used to list all states"""
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CityView(APIView):
    def get(self, request):
        """Used to list all cities"""
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CountryStateView(APIView):
    def get(self, request, pk):
        try:
            country = Country.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response({"message": "This country is not supported yet"}, status.HTTP_404_NOT_FOUND)
        country_states = country.country_states.all()
        serializer = StateSerializer(country_states, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class StateCityView(APIView):
    def get(self, request, pk):
        try:
            state = State.objects.get(id=pk)
        except State.DoesNotExist:
            return Response({"message": "This state does not exist or is not supported yet"}, status.HTTP_404_NOT_FOUND)
        cities = state.state_cities.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status.HTTP_200_OK)