from django.db import models

from example.powertables.models import PowerTableModel


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
