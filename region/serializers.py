from rest_framework import serializers
from .models import *


class RegionSerializer(serializers.ModelSerializer):
    class meta:
        model = Region
        fields = "__all__"