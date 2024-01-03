from rest_framework import serializers
from .models import Country
from region.models import Region


class CountrySerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(
        slug_field="name", queryset=Region.objects.all())

    class Meta:
        model = Country
        fields = "__all__"
