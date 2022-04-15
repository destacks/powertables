# Usage:
# - ". venv/bin/activate"
# - "python manage.py shell < generate_fake_data.py"
import random

from contacts.models import Company, Contact, Position
from faker import Faker

fake = Faker()
n = 250
m = 10000

print("\nSTART Bulk create companies.")
company_names = []
for index in range(0, n):
    name = fake.company()
    company_names.append(name)
company_names = set(company_names)
companies = []
for name in company_names:
    companies.append(Company(name=name))
Company.objects.bulk_create(companies)
companies = list(Company.objects.all())
print("END Bulk create companies.")


print("\nSTART Bulk create positions.")
position_names = []
for index in range(0, n):
    name = fake.job()
    position_names.append(name)
position_names = set(position_names)
positions = []
for name in position_names:
    positions.append(Position(name=name))
Position.objects.bulk_create(positions)
positions = list(Position.objects.all())
print("END Bulk create positions.")


print("\nSTART Bulk create contacts.")
contacts = []
for index in range(0, m):
    contact = Contact(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        company=random.choice(companies),
        position=random.choice(positions),
        email=fake.email(),
    )
    contacts.append(contact)

Contact.objects.bulk_create(contacts)
print("END Bulk create contacts.\n")
