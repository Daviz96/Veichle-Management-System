import django
from random import choice
from django.conf import settings
from random import randint

settings.configure(
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "VMS_db",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    },
    INSTALLED_APPS=["vms_app"],
)

django.setup()

from vms_app.models import Vehicle
from django.db import transaction



# Create a list of 10 real-life vehicle models
models = [
    "Ford Fusion",
    "Toyota Camry",
    "Honda Civic",
    "Nissan Altima",
    "Chevrolet Malibu",
    "Hyundai Sonata",
    "Mazda 6",
    "Subaru Outback",
    "Kia Optima",
    "Jeep Grand Cherokee",
]

# Generate a list of 100 registration plates
registration_plates = [f"AB{i:04d}" for i in range(100)]

# Create a list of 100 vehicle objects with different registration plates
# and a randomly chosen model from the list above
vehicles = [
    Vehicle(
        model=models[randint(0, len(models)-1)],
        registration_plate=plate,
        vehicle_status=choice(Vehicle.VEHICLE_STATUS_CHOICES)[0],
        fuel_type=choice(Vehicle.FUEL_TYPE_CHOICES)[0],
        insurance_status=choice(Vehicle.INSURANCE_STATUS_CHOICES)[0],
        inspection_status=choice(Vehicle.INSPECTION_STATUS_CHOICES)[0],
    )
    for plate in registration_plates
]

# Use a transaction to insert the vehicles into the database
with transaction.atomic():
    for vehicle in vehicles:
        vehicle.save()
