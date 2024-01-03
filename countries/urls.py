from django.urls import path
from .views import *


urlpatterns = [
    path("", AllCountries.as_view()),
    path("add-countries/", AddCountries.as_view()),
]
