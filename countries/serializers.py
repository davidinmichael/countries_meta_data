from rest_framework import serializers
from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"
        

class CountrySerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    region = RegionSerializer()

    class Meta:
        model = Country
        fields = ["id", "name", "capital", "phone_code", "latitude", "longitude",
                  "iso2", "iso3", "flag", "currency", "region"]

    def to_representation(self, instance):
        country = super().to_representation(instance)
        country["phone_code"] = f"+{country['phone_code']}"
        return country


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = State
        fields = ["id", "name", "latitude", "longitude", "identifier", "state_code",
                  "country"]


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = "__all__"
