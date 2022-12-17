from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.http import HttpResponse
from .models import Driver, DriverLicense, Vehicle, Address, Path

from .forms import DriverAddForm, DriverLicenseAddForm, VehicleAddForm, AddressForm

# Create your views here.


def user(request):
    if request.user.is_authenticated:
        user = request.user
        return user
    return ""

class Home(View):
    def get(self, request):
        return render(request, "vms-home.html", {"user": user(request)})


class DriversView(View):

    def get(self, request):
        drivers = Driver.objects.all()
        context = {
            'drivers': drivers,
            "user": user(request)
        }
        return render(request, 'vms-drivers-list.html', context)


class DriverDetailsView(View):
    def get(self, request, id):
        driver = Driver.objects.get(pk=id)
        license = DriverLicense.objects.get(driver=driver)
        context = {
            'driver': driver,
            'license': license,
            "user": user(request)
        }
        return render(request, "vms-driver-details.html", context)


class DriverEditView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        return render(request, "vms-driver-edit.html", {"user": user(request)})


class DriverDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        driver = Driver.objects.get(pk=id)
        driver.delete()
        return redirect("driver-list")


class DriverAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        form_driver = DriverAddForm()
        form_license = DriverLicenseAddForm()
        return render(request, "vms-driver-add.html", {"user": user(request), "form_driver": form_driver, "form_license": form_license})

    def post(self, request):
        form_driver = DriverAddForm(request.POST)
        form_license = DriverLicenseAddForm(request.POST)
        if form_driver.is_valid() and form_license.is_valid():

            firstName = form_driver.cleaned_data['firstName']
            lastName = form_driver.cleaned_data['lastName']
            nationalId = form_driver.cleaned_data['nationalId']
            address = form_driver.cleaned_data['address']
            birth_date = form_driver.cleaned_data['birth_date']
            email = form_driver.cleaned_data['email']
            phoneNumber = form_driver.cleaned_data['phoneNumber']
            status = form_driver.cleaned_data['status']

            serial_id = form_license.cleaned_data['serial_id']
            release_date = form_license.cleaned_data['release_date']
            expiration_date = form_license.cleaned_data['expiration_date']

            try:
                driver = Driver.objects.create(firstName=firstName, lastName=lastName, nationalId=nationalId,
                                                address=address, birth_date=birth_date, email=email, phoneNumber=phoneNumber,
                                                status=status)
            except Exception as e:
                return HttpResponse(f"{e}")

            try:
                license = DriverLicense.objects.create(driver=driver, serial_id=serial_id, release_date=release_date,
                                                       expiration_date=expiration_date)
            except Exception as e:
                return HttpResponse(f"{e}")

            return redirect(reverse('driver-details', kwargs={'id': driver.pk}))
        else:
            return HttpResponse("form is not valid")


class VehiclesView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        context = {
            'vehicles': vehicles,
            "user": user(request)
        }
        return render(request, "vms-vehicles-list.html", context)



class VehicleDetailsView(View):
    def get(self, request, id):
        vehicle = Vehicle.objects.get(pk=id)
        context = {
            'vehicle': vehicle,
            "user": user(request)
        }
        return render(request, "vms-vehicle-details.html", context)


class VehicleEditView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        return render(request, "vms-vehicle-edit.html", {"user": user(request)})


class VehicleAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = VehicleAddForm()
        context = {
            "user": user(request),
            "form": form
        }
        return render(request, "vms-vehicle-add.html", context)


    def post(self, request):
        form = VehicleAddForm(request.POST)
        if form.is_valid():

            model = form.cleaned_data['model']
            registration_plate = form.cleaned_data['registration_plate']
            vehicle_status = form.cleaned_data['vehicle_status']
            fuel_type = form.cleaned_data['fuel_type']
            insurance_status = form.cleaned_data['insurance_status']
            inspection_status = form.cleaned_data['inspection_status']

            vehicle = Vehicle.objects.create(model=model, registration_plate=registration_plate,
                                            vehicle_status=vehicle_status,fuel_type=fuel_type,
                                            insurance_status=insurance_status, inspection_status=inspection_status)

            return redirect(reverse('vehicle-details', kwargs={'id': vehicle.pk}))
        else:
            return HttpResponse("form is not valid")


class VehicleDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        vehicle = Vehicle.objects.get(pk=id)
        vehicle.delete()
        return redirect("vehicle-list")


class PathsView(View):
    def get(self, request):
        paths = Path.objects.all()
        context = {
            'paths': paths,
            "user": user(request)
        }
        return render(request, "vms-paths-list.html", context)


class PathDetailsView(View):
    def get(self, request, id):
        path = Path.objects.get(pk=id)
        context = {
            "path": path,
            "user": user(request)
        }
        return render(request, "vms-path-details.html", context)


class PathAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        form_start = AddressForm()
        form_end = AddressForm()
        vehicles = Vehicle.objects.filter(vehicle_status="NW")
        drivers = Driver.objects.filter(status="NW")
        context = {
            "user": user(request),
            "form_start": form_start,
            "form_end": form_end,
            "drivers": drivers,
            "vehicles": vehicles,
        }
        return render(request, "vms-path-add.html", context)

    def post(self, request):

        start_state = request.POST.get("state_start")
        start_city = request.POST.get("city_start")
        start_address = request.POST.get("address_start")
        start_postal_code = request.POST.get("postal_code_start")

        end_state = request.POST.get("state_end")
        end_city = request.POST.get("city_end")
        end_address = request.POST.get("address_end")
        end_postal_code = request.POST.get("postal_code_end")

        driver = request.POST.get("drivers")
        print(Driver.objects.get(nationalId=driver))
        vehicle = request.POST.get("cars")
        print(vehicle)
        date = request.POST.get("date")
        print(date)

        path_address_start = Address.objects.create(state=start_state, city=start_city, address=start_address, postal_code=start_postal_code)
        path_address_end = Address.objects.create(state=end_state, city=end_city, address=end_address, postal_code=end_postal_code)

        print(path_address_start)
        print(path_address_end)

        driver_obj = Driver.objects.get(nationalId=driver)
        vehicle_obj = Vehicle.objects.get(registration_plate=vehicle)

        driver_obj.status = "W"
        vehicle_obj.vehicle_status = "W"
        driver_obj.save()
        vehicle_obj.save()

        path = Path.objects.create(start=path_address_start, end=path_address_end, driver=driver_obj, vehicle=vehicle_obj, date=date)

        return redirect(reverse('path-details', kwargs={'id': path.pk}))



class PathDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        path = Path.objects.get(pk=id)
        driver = path.driver
        vehicle = path.vehicle

        driver.status = "NW"
        driver.save()
        vehicle.vehicle_status = "NW"
        vehicle.save()

        path.delete()

        return redirect("path-list")

