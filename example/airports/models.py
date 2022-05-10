from django.db import models
from powertables.models import PowertableModel


class Iata(PowertableModel):
    pass


class Icao(PowertableModel):
    pass


class City(PowertableModel):
    pass


class State(PowertableModel):
    pass


class Country(PowertableModel):
    pass


class Airport(PowertableModel):
    iata = models.ForeignKey(Iata, on_delete=models.DO_NOTHING)
    icao = models.ForeignKey(Icao, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
