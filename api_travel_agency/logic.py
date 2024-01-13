from .models import Holiday, Location, Reservation
from .serializers import VacationEncoder, PlaceEncoder, BookingEncoder
from django.core import serializers


def create_holiday(request):
    title = request.data.get('title')
    start_date = request.data.get('start_date')
    duration = request.data.get('duration')
    price = request.data.get('price')
    free_slots = request.data.get('free_slots')
    auto_inc_id = request.data.get('id')

    try:
        location_obj = Location.objects.get(auto_increment_id=auto_inc_id)
        holiday = Holiday(
            location=location_obj,
            title=title,
            start_date=start_date,
            duration=duration,
            price=price,
            free_slots=free_slots,
        )
        holiday.save()
        return {'Success': 'A holiday was established!'}
    except Location.DoesNotExist:
        return {'Error': 'No location exists with this id!'}
    except Exception:
        return {'Error': 'An issue occurred during the holiday creation process!'}


def delete_holiday(request):
    holiday_id = request.data.get('id')

    try:
        holiday = Holiday.objects.get(auto_increment_id=holiday_id)
        holiday.delete()
        return {'Success': 'Holiday deleted'}
    except Holiday.DoesNotExist:
        return {'Error': 'No holiday exists with this id!'}
    except Exception:
        return {'Error': 'An issue occurred during the holiday deletion process!'}


def get_all_holidays(request):
    holidays = Holiday.objects.all()
    serialized = VacationEncoder(holidays, many=True)
    return serialized


def get_holiday_by_id(request):
    holiday_id = request.data.get('id')

    try:
        holiday = Holiday.objects.get(auto_increment_id=holiday_id)
        return VacationEncoder(holiday, many=False)
    except Holiday.DoesNotExist:
        return {'Error': 'No holiday exists with this id!'}
    except Exception:
        return {'Error': 'An issue occurred while retrieving the holiday!'}


def edit_holiday(request):
    holiday_id = request.data.get('id')
    location_id = request.data.get('location')
    title = request.data.get('title')
    start_date = request.data.get('start_date')
    duration = request.data.get('duration')
    price = request.data.get('price')
    free_slots = request.data.get('free_slots')

    try:
        obj = Holiday.objects.get(auto_increment_id=holiday_id)
        if location_id:
            try:
                new_location = Location.objects.get(auto_increment_id=location_id)
                obj.location = new_location
            except Exception:
                return {'Error': 'No location exists with this id!'}
        if title:
            obj.title = title
        if start_date:
            obj.start_date = start_date
        if duration:
            obj.duration = duration
        if price:
            obj.price = price
        if free_slots:
            obj.free_slots = free_slots
        obj.save()
        return VacationEncoder(obj)
    except Exception:
        return {'Error': 'No holiday exists with this id!'}


# ---- Location ---- #
def create_location(request):
    number = request.data.get('number')
    country = request.data.get('country')
    city = request.data.get('city')
    image_url = request.data.get('image_url')

    try:
        location = Location(
            number=number,
            country=country,
            city=city,
            image_url=image_url,
        )
        location.save()
        return {'Success': 'A location was established!'}
    except Location.DoesNotExist:
        return {'Error': 'No location exists with this id!'}
    except Exception:
        return {'Error': 'An issue occurred during the location creation process!'}


def delete_location(request):
    location_id = request.data.get('id')

    try:
        location = Location.objects.get(auto_increment_id=location_id)
        location.delete()
        return True
    except Exception:
        return False


def get_all_locations(request):
    locations = Location.objects.all()
    serialized = PlaceEncoder(locations, many=True)
    return serialized


def get_location_by_id(request):
    location_id = request.data.get('id')

    try:
        location = Location.objects.get(auto_increment_id=location_id)
        return PlaceEncoder(location)
    except Exception:
        return {'Error': f'The location with the specified id {location_id} does not exist!'}


def edit_location(request):
    number = request.data.get('number')
    country = request.data.get('country')
    city = request.data.get('city')
    image_url = request.data.get('image_url')
    loc_id = request.data.get('id_loc')

    try:
        obj = Location.objects.get(auto_increment_id=loc_id)
        if number:
            obj.number = number
        if country:
            obj.country = country
        if city:
            obj.city = city
        if image_url:
            obj.image_url = image_url
        return PlaceEncoder(obj)
    except Exception:
        return False


# ---- Reservation ---- #
def create_reservation(request):
    contact_name = request.data.get('contact_name')
    phone_number = request.data.get('phone_number')
    holiday_id = request.data.get('holiday_id')
    location_id = request.data.get('location_id')

    try:
        holiday_obj = Holiday.objects.get(auto_increment_id=holiday_id)
        location_obj = Location.objects.get(auto_increment_id=location_id)
        reservation = Reservation(
            contact_name=contact_name,
            phone_number=phone_number,
            holiday=holiday_obj,
            location=location_obj
        )
        reservation.save()
        return {'Success': 'reservation created '}
    except Location.DoesNotExist:
        return {'Error': 'No location exists with this id!'}
    except Exception:
        return {'Error': 'An issue occurred during the reservation creation process!'}



def delete_reservation(request):
    reserve_id = request.data.get('reservation_id')
    try:
        reseve_obj = Reservation.objects.get(auto_increment_id=reserve_id)
        reseve_obj.delete()
        return {'Success': 'deleted'}
    except Exception:
        return {'Error': 'Unable to locate a reservation with that id!'}


def get_all_reservations(request):
    reservations = Reservation.objects.all()
    serialized = BookingEncoder(reservations, many=True)
    return serialized


def get_reservation_by_id(request):
    reserve_id = request.data.get('reservation_id')
    try:
        reserve_obj = Reservation.objects.get(auto_increment_id=reserve_id)
        serialized = BookingEncoder(reserve_obj)
        return serialized
    except Exception:
        return {'Error': 'No reservation exists with this id!'}


def edit_reservation(request):
    reserve_id = request.data.get('reservation_id')
    holiday_id = request.data.get('holiday_id')
    phone_number = request.data.get('phone_number')
    location_id = request.data.get('location_id')
    contact_name = request.data.get('contact_name')

    try:
        obj = Reservation.objects.get(auto_increment_id=reserve_id)
        if contact_name:
            obj.contact_name = contact_name
        if phone_number:
            obj.phone_number = phone_number
        if holiday_id:
            try:
                holiday_obj = Holiday.objects.get(auto_increment_id=holiday_id)
            except Exception:
                return {'Error': 'No holiday exists with this id!'}
            obj.holiday = holiday_obj
        if location_id:
            try:
                location_obj = Location.objects.get(auto_increment_id=location_id)
            except Exception:
                return {'Error': 'No location exists with this id!'}
            obj.location = location_obj
        obj.save()
        return BookingEncoder(obj)
    except Exception:
        return False
