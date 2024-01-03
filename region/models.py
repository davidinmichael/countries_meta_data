from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=50)
    wiki_data_Id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
