from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name
