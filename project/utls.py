from django.contrib.auth.models import Group
from .exceptions import BadRequestException


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