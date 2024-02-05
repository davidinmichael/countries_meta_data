from rest_framework import serializers
from .models import Country
from region.models import Region
from region.serializers import *


class CountrySerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    class Meta:
        model = Country
        fields = "__all__"
