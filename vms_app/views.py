from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, "__base__.html")


class DriversView(View):
    def get(self, request):
        return render(request, "vms-drivers-list.html")


class DriverDetailsView(View):
    def get(self, request):
        return render(request, "vms-driver-details.html")


class DriverEditView(View):
    def get(self, request):
        return render(request, "vms-driver-edit.html")


class DriverAddView(View):
    def get(self, request):
        return render(request, "vms-driver-add.html")


class VehiclesView(View):
    def get(self, request):
        return render(request, "vms-vehicles-list.html")


class VehicleDetailsView(View):
    def get(self, request):
        return render(request, "vms-vehicle-details.html")


class VehicleEditView(View):
    def get(self, request):
        return render(request, "vms-vehicle-edit.html")


class VehicleAddView(View):
    def get(self, request):
        return render(request, "vms-vehicle-add.html")


class PathsView(View):
    def get(self, request):
        return render(request, "vms-paths-list.html")


class PathDetailsView(View):
    def get(self, request):
        return render(request, "vms-path-details.html")


class PathAddView(View):
    def get(self, request):
        return render(request, "vms-path-add.html")