# Usage:
# - ". venv/bin/activate"
# - "python manage.py shell < generate_fake_data.py"
import random

from airports.models import Airport, City, Country, Iata, Icao, State
from django.db.utils import IntegrityError
from faker import Faker
from faker_airtravel import AirTravelProvider

fake = Faker()
fake.add_provider(AirTravelProvider)

n = 1000

print("\n-- START airports creation --\n")

airports = []
counter = 1
for index in range(0, n):
    try:
        flight = fake.flight()
        airport_obj = fake.airport_object()

        name = airport_obj["airport"]
        if not name:
            continue

        iata_name = airport_obj["iata"]
        if not iata_name:
            continue
        iata = Iata.objects.get_or_create(name=iata_name)[0]

        icao_name = airport_obj["icao"]
        if not icao_name:
            continue
        icao = Icao.objects.get_or_create(name=icao_name)[0]

        city_name = airport_obj["city"]
        if not city_name:
            continue
        city = City.objects.get_or_create(name=city_name)[0]

        state_name = airport_obj["state"]
        if not state_name:
            continue
        state = State.objects.get_or_create(name=state_name)[0]

        country_name = airport_obj["country"]
        if not country_name:
            continue
        country = Country.objects.get_or_create(name=country_name)[0]

        airport = Airport.objects.get_or_create(
            name=name,
            iata=iata,
            icao=icao,
            city=city,
            state=state,
            country=country,
        )
        airports.append(airport)

        print(counter, "of", n, airport)
        counter += 1
    except IntegrityError:
        print("IntegrityError for", airport_obj)

print("\n-- END airports creation --\n")
