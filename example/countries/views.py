from django.views.generic import ListView

from .models import Country


class CountryListView(ListView):
    model = Country
