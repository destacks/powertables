from django.urls import path

from .views import AirportPowerTableView

app_name = "airports"
urlpatterns = [
    path("", AirportPowerTableView.as_view(), name="list"),
]
