from example.powertables.views import PowerTableView

from .models import Airport


class AirportPowerTableView(PowerTableView):
    model = Airport
