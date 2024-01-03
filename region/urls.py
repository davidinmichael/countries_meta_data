from django.urls import path
from .views import *

urlpatterns = [
    path("", RegionList.as_view()),
    # path("add-region/", AddRegion.as_view()),
]
