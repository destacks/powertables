from example.powertables.views import PowertableView

from .models import Airport


class AirportPowertableView(PowertableView):
    model = Airport
