from django.urls import path

from .views import ContactPowerTableView

app_name = "contacts"
urlpatterns = [
    path("", ContactPowerTableView.as_view(), name="list"),
]
