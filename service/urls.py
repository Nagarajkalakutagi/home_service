from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('city', Cities, basename='city')
router.register('service', Services, basename='service')
router.register('service_type', ServiceTypes, basename='service_type')
router.register('service_charge', ServiceCharges, basename='service_charge')
router.register('service_provider', ServiceProviders, basename='service_provider')
router.register('book_appointment', BookAppointments, basename='bookAppointment')
router.register('contacts', Contacts, basename='contacts')


register = DefaultRouter()
register.register('user', RegisterUser, basename='register_user')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', include(register.urls)),
]
