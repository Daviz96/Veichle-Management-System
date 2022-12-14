from django.db import models

# Create your models here.


class DriverLicense(models.Model):
    driver = models.OneToOneField("Driver", default=None, on_delete=models.CASCADE)
    serial_id = models.CharField(max_length=20, unique=True)
    release_date = models.DateField(default=None)
    expiration_date = models.DateField(default=None)


class Driver(models.Model):

    STATUS_CHOICES = (
        ('W', 'Work'),
        ('NW', 'Not Work'),
    )

    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    nationalId = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=1000)
    birth_date = models.DateField(default=None)
    email = models.CharField(max_length=300)
    phoneNumber = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NW')

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


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

    driver = models.ForeignKey(Driver, default=None, on_delete=models.PROTECT, null=True)
    model = models.CharField(max_length=200, default='')
    registration_plate = models.CharField(max_length=200, default=None, unique=True, null=True)
    vehicle_status = models.CharField(max_length=2, default='NW', choices=VEHICLE_STATUS_CHOICES)
    fuel_type = models.CharField(max_length=1, default='P', choices=FUEL_TYPE_CHOICES)
    # mileage = models.DecimalField(max_digits=20, default=0, decimal_places=0)
    insurance_status = models.CharField(max_length=2, default='NU', choices=INSURANCE_STATUS_CHOICES)
    inspection_status = models.CharField(max_length=2, default='NU', choices=INSPECTION_STATUS_CHOICES)

    def __str__(self):
        return f"{self.model} {self.registration_plate}"


class Address(models.Model):
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.address},{self.postal_code},{self.city},{self.state}"


class Path(models.Model):
    driver = models.ForeignKey(Driver, default=None, on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.PROTECT)
    start = models.ForeignKey(Address, default=None, related_name='start', on_delete=models.PROTECT)
    end = models.ForeignKey(Address, default=None, related_name='end', on_delete=models.PROTECT)
    date = models.DateField(default=None)








