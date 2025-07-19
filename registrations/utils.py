from rest_framework.exceptions import ValidationError
from project.utls import validate_egyptian_id

def validate_user_data(user, id_number, id_front, id_back):
    errors = {}

    if not user.id_number and not id_number:
        errors["id_number"] = {
            "en": "ID number is required.",
            "ar": "الرقم القومي مطلوب."
        }
    elif id_number:
        is_valid, message = validate_egyptian_id(id_number)
        if not is_valid:
            errors["id_number"] = {
                "en": message,
                "ar": "الرقم القومي غير صالح."
            }
        else:
            user.id_number = id_number

    if not user.id_front and not id_front:
        errors["id_front"] = {
            "en": "Front ID image is required.",
            "ar": "صورة الوجه للبطاقة مطلوبة."
        }
    elif id_front:
        user.id_front = id_front

    if not user.id_back and not id_back:
        errors["id_back"] = {
            "en": "Back ID image is required.",
            "ar": "صورة الخلف للبطاقة مطلوبة."
        }
    elif id_back:
        user.id_back = id_back

    if errors:
        raise ValidationError(errors)

    user.save()
