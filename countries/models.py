from django.db import models
from region.models import Region


class Country(models.Model):
    name = models.CharField(max_length=50)
    capital = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso2 = models.CharField(max_length=5)
    iso3 = models.CharField(max_length=5)
    numeric_code = models.CharField(max_length=10)
    phone_code = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    currency_name = models.CharField(max_length=10)
    flag = models.SlugField(max_length=50)

    def generate_flag_url(self):
        return f"https://flagcdn.com/256x192/{self.iso2.lower()}.png"

    def save(self, *args, **kwargs):
        if not self.flag:
            self.flag = self.generate_flag_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} | {self.capital}"
