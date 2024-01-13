from rest_framework import serializers
from api_travel_agency.models import Holiday, Location, Reservation


class VacationEncoder(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = '__all__'
        
class PlaceEncoder(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        
        
class BookingEncoder(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'