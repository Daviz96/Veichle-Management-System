from django.db import models

# Create your models here.


class DriverLicense(models.Model):
    driver = models.OneToOneField("Driver", default=None, on_delete=models.PROTECT)
    serial_id = models.CharField(max_length=20)
    release_date = models.DateField(default=None)
    expiration_date = models.DateField(default=None)


class Driver(models.Model):

    STATUS_CHOICES = (
        ('W', 'Work'),
        ('NW', 'Not Work'),
    )

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nationalId = models.CharField(max_length=13)
    address = models.CharField(max_length=1000)
    birth_date = models.DateField(default=None)
    email = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=10)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NW')


class Vehicle(models.Model):
    VEHICLE_STATUS_CHOICES = (
        ('W', 'Work'),
        ('NW', 'Not Work'),
    )
    INSURANCE_STATUS_CHOICES = (
        ('U', 'Updated'),
        ('NU', 'Not Updated'),
    )

    INSPECTION_STATUS_CHOICES = (
        ('U', 'Updated'),
        ('NU', 'Not Updated'),
    )

    FUEL_TYPE_CHOICES = (
        ('P', 'Petrol'),
        ('D', 'Diesel'),
    )

    driver = models.ForeignKey(Driver, default=None, on_delete=models.CASCADE)
    registration_plate = models.CharField(max_length=200, default='')
    vehicle_status = models.CharField(max_length=2, default='NW', choices=VEHICLE_STATUS_CHOICES)
    fuel_type = models.CharField(max_length=1, default='P', choices=FUEL_TYPE_CHOICES)
    # mileage = models.DecimalField(max_digits=20, default=0, decimal_places=0)
    insurance_status = models.CharField(max_length=2, default='NU', choices=INSURANCE_STATUS_CHOICES)
    inspection_status = models.CharField(max_length=2, default='NU', choices=INSPECTION_STATUS_CHOICES)


class Address(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)


class Path(models.Model):
    driver = models.ForeignKey(Driver, default=None, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE)
    start = models.ForeignKey(Address, default=None, related_name='start', on_delete=models.CASCADE)
    end = models.ForeignKey(Address, default=None, related_name='end', on_delete=models.CASCADE)






