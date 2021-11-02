from random import random
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from authentication.backend import RegisterAuthBackend
from .serializers import *
from .models import *


class RegisterUser(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @staticmethod
    def create(request):
        data = request.data
        auth = RegisterAuthBackend()

        if auth.get_user(data['email']):
            return Response({"msg": "email is already exist", "code": 409}, status=HTTP_409_CONFLICT)
        elif auth.get_phone(data['mobile']):
            return Response({"msg": "mobile number is already exist", "code": 409}, status=HTTP_409_CONFLICT)
        else:
            otp = random.randint(1000, 9999)
            # send = send_otp(data['mobile'], otp)
            return Response("send", status=HTTP_200_OK)


class Cities(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class Services(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceTypes(viewsets.ModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceType.objects.all()


class ServiceCharges(viewsets.ModelViewSet):
    serializer_class = ServiceChargeSerializer
    queryset = ServiceCharge.objects.all()


class ServiceProviders(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()


class BookAppointments(viewsets.ModelViewSet):
    serializer_class = BookAppointmentSerializer
    queryset = BookAppointment.objects.all()


class Contacts(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()