from django.db import models

from .utils import get_model_fields


class PowerTableManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .order_by(*get_model_fields(self.model, option="name"))
        )


class PowerTableModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    objects = PowerTableManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    __repr__ = __str__


class Iata(PowerTableModel):
    pass


class Icao(PowerTableModel):
    pass


class City(PowerTableModel):
    pass


class State(PowerTableModel):
    pass


class Country(PowerTableModel):
    pass


class Airport(PowerTableModel):
    iata = models.ForeignKey(Iata, on_delete=models.DO_NOTHING)
    icao = models.ForeignKey(Icao, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
