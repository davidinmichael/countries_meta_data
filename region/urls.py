from django.urls import path
from .views import *

urlpatterns = [
    path("", RegionList.as_view()),

    # URL for addidng Regions to the DB
    # path("add-region/", AddRegion.as_view()),
]
