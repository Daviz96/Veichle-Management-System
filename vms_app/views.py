from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import Driver, DriverLicense, Vehicle, Address, Path

# Create your views here.
class BaseView(View):
    def get(self, request):
        user_auth = request.user.is_authenticated
        user = request.user
        context = {
            "user_auth": user_auth,
            "user": user
        }
        return render(request, context)


class Home(View):
    def get(self, request):
        # user_auth = request.user.is_authenticated
        # user = request.user
        # context = {
        #     "user_auth": user_auth,
        #     "user": user
        # }
        return render(request, "vms-home.html")


class DriversView(View):

    def get(self, request):
        drivers = Driver.objects.all()
        context = {
            'drivers': drivers
        }
        return render(request, 'vms-drivers-list.html', context)


class DriverDetailsView(View):
    def get(self, request, id):
        driver = Driver.objects.get(pk=id)
        license = DriverLicense.objects.get(driver=driver)
        context = {
            'driver': driver,
            'license': license
        }
        return render(request, "vms-driver-details.html", context)


class DriverEditView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        return render(request, "vms-driver-edit.html")


class DriverDeleteView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        driver = Driver.objects.get(pk=id)
        driver.delete()
        return redirect("driver-list")


class DriverAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "vms-driver-add.html")


class VehiclesView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        context = {
            'vehicles': vehicles
        }
        return render(request, "vms-vehicles-list.html", context)



class VehicleDetailsView(View):
    def get(self, request, id):
        return render(request, "vms-vehicle-details.html")


class VehicleEditView(View):
    @method_decorator(login_required)
    def get(self, request, id):
        return render(request, "vms-vehicle-edit.html")


class VehicleAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "vms-vehicle-add.html")


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
            'paths': paths
        }
        return render(request, "vms-paths-list.html", context)


class PathDetailsView(View):
    def get(self, request, id):
        return render(request, "vms-path-details.html")


class PathAddView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "vms-path-add.html")