from django import forms
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


# class VehicleAddForm(forms.Form):
#     class DriverAddForm(forms.Form):

# years=(year for year in range(datetime.date.today().year, 1900, -1)