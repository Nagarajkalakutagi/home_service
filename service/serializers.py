from rest_framework.serializers import ModelSerializer
from .models import *


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'


class ServiceChargeSerializer(ModelSerializer):
    class Meta:
        model = ServiceCharge
        fields = '__all__'


class ServiceProviderSerializer(ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'


class BookAppointmentSerializer(ModelSerializer):
    class Meta:
        model = BookAppointment
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CallbackRequestSerializer(ModelSerializer):
    class Meta:
        model = CallbackRequest
        fields = '__all__'