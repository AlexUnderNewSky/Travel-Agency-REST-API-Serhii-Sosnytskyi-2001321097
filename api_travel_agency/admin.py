from django.contrib import admin
from .models import Holiday, Location, Reservation


@admin.register(Holiday)
class VacationAdmin(admin.ModelAdmin):
    list_display = ['auto_increment_id', 'location', 'title', 'start_date', 'duration', 'price', 'free_slots']


@admin.register(Location)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['auto_increment_id', 'street', 'number', 'city', 'country', 'image_url']

@admin.register(Reservation)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['auto_increment_id', 'contact_name', 'phone_number', 'holiday']
