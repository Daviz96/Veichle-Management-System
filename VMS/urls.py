"""VMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from django.urls import path, include

import vms_app.views as v
import accounts.views as a

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('accounts/', include('django.contrib.auth.urls')),

    path('login/', a.LoginView.as_view(), name='login'),
    path('logout/', a.LogoutView.as_view(), name='logout'),
    path('register/', a.RegisterView.as_view(), name='register'),

    path('', v.Home.as_view(), name='home'),

    path('driver/list/', v.DriversView.as_view(), name='driver-list'),
    path('driver/<int:id>/', v.DriverDetailsView.as_view(), name='driver-details'),
    path('driver/edit/<int:id>/', v.DriverEditView.as_view(), name='driver-edit'),
    path('driver/add/', v.DriverAddView.as_view(), name='driver-add'),
    path('driver/delete/<int:id>/', v.DriverDeleteView.as_view(), name='driver-delete'),

    path('vehicle/list/', v.VehiclesView.as_view(), name='vehicle-list'),
    path('vehicle/<int:id>/', v.VehicleDetailsView.as_view(), name='vehicle-details'),
    path('vehicle/edit/<int:id>/', v.VehicleEditView.as_view(), name='vehicle-edit'),
    path('vehicle/add/', v.VehicleAddView.as_view(), name='vehicle-add'),
    path('vehicle/delete/<int:id>/', v.VehicleDeleteView.as_view(), name='vehicle-delete'),

    path('path/list/', v.PathsView.as_view(), name='path-list'),
    path('path/<int:id>/', v.PathDetailsView.as_view(), name='path-details'),
    path('path/add/', v.PathAddView.as_view(), name='path-add'),


]
