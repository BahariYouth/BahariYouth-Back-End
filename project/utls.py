from django.contrib.auth.models import Group
from .exceptions import BadRequestException
import datetime
import re

def validate_egyptian_id(id_number):
    if not re.fullmatch(r"\d{14}", id_number):
        return False, "ID must be 14 digits."

    century = int(id_number[0])
    year = int(id_number[1:3])
    month = int(id_number[3:5])
    day = int(id_number[5:7])
    governorate = int(id_number[7:9])

    if century not in [2, 3]:
        return False, "Invalid century digit."

    full_year = (1900 if century == 2 else 2000) + year
    
    try:
        datetime.date(full_year, month, day)
    except ValueError:
        return False, "Invalid birth date in ID."

    valid_governorates = list(range(1, 36)) 
    if governorate not in valid_governorates:
        return False, "Invalid governorate code."

    return True, "Valid Egyptian ID."





def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def add_user_to_group(user, group_name):
    group, created = Group.objects.get_or_create(name=group_name)
    user.groups.add(group)
    user.save()
    return user

def get_request_data_or_400(request, key, error_message=None):
    if key not in request.data:
        raise BadRequestException({
            'status' : 'error',
            'message' : error_message or f"{key} is required.",
            'error' : error_message or f"{key} is required."
        })
    return request.data[key]