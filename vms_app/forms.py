from django import forms
from .models import Driver, Vehicle
import datetime


# class AddressForm(forms.Form):
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput())
#     address_1 = forms.CharField(
#         label='Address',
#         widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
#     )
#     address_2 = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
#     )
#     city = forms.CharField()
#     state = forms.ChoiceField(choices=STATES)
#     zip_code = forms.CharField(label='Zip')
#     check_me_out = forms.BooleanField(required=False)


class DriverAddForm(forms.Form):
    STATUS_CHOICES = (
        ('', 'Choose...'),
        ('W', 'Work'),
        ('NW', 'Not Work'),
    )

    firstName = forms.CharField(label='First Name')
    lastName = forms.CharField(label='Last Name')
    nationalId = forms.CharField(label='National ID')
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    birth_date = forms.DateField(label='Birth Date', widget=forms.SelectDateWidget(years=(year for year in range(2022, 1900, -1))))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phoneNumber = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder': '+48 488 588 688'}))
    status = forms.ChoiceField(label='Status', choices=STATUS_CHOICES)


class DriverLicenseAddForm(forms.Form):
    serial_id = forms.CharField(label='Serial ID')
    release_date = forms.DateField(label='Release Date', widget=forms.SelectDateWidget(years=(year for year in range(2022, 1900, -1))))
    expiration_date = forms.DateField(label='Expiration Date', widget=forms.SelectDateWidget(years=(year for year in range(2022, 1900, -1))))

# years=(year for year in range(datetime.date.today().year, 1900, -1)

class VehicleAddForm(forms.Form):
    VEHICLE_STATUS_CHOICES = (
        ('', 'Choose...'),
        ('W', 'Work'),
        ('NW', 'Not Work'),
    )
    INSURANCE_STATUS_CHOICES = (
        ('', 'Choose...'),
        ('U', 'Updated'),
        ('NU', 'Not Updated'),
    )

    INSPECTION_STATUS_CHOICES = (
        ('', 'Choose...'),
        ('U', 'Updated'),
        ('NU', 'Not Updated'),
    )

    FUEL_TYPE_CHOICES = (
        ('', 'Choose...'),
        ('P', 'Petrol'),
        ('D', 'Diesel'),
    )

    model = forms.CharField(label="Model")
    registration_plate = forms.CharField(label="Registration Plate")
    vehicle_status = forms.ChoiceField(label="Vehicle Status", choices=VEHICLE_STATUS_CHOICES)
    fuel_type = forms.ChoiceField(label="Fuel Type", choices=FUEL_TYPE_CHOICES)
    insurance_status = forms.ChoiceField(label="Insurance Status", choices=INSURANCE_STATUS_CHOICES)
    inspection_status = forms.ChoiceField(label="Inspection Status", choices=INSPECTION_STATUS_CHOICES)


class AddressForm(forms.Form):
    state = forms.CharField(label="State")
    city = forms.CharField(label="City")
    address = forms.CharField(label="Address")
    postal_code = forms.CharField(label="Postal Code")


class PathForm(forms.Form):
    drivers = list(Driver.objects.filter(status="NW"))
    vehicles = list(Vehicle.objects.filter(vehicle_status="NW"))
    DRIVER_CHOICES = [tuple([driver.pk, driver.lastName])for driver in drivers]
    VEHICLE_CHOICES = [tuple([vehicle.pk, vehicle.registration_plate])for vehicle in vehicles]


    driver = forms.ChoiceField(label="Driver", choices=DRIVER_CHOICES)
    vehicle = forms.ChoiceField(label="Vehicle", choices=VEHICLE_CHOICES)

