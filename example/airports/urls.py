from django.urls import path

from .views import AirportPowertableView

app_name = "airports"
urlpatterns = [
    path("", AirportPowertableView.as_view(), name="list"),
]
