import csv # For CSV export
from django.contrib import admin
from django.http import HttpResponse
from .models import RegisterationEvents, RegisterationActivities
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from io import BytesIO
import requests
from django.utils.html import format_html
from PIL import Image


class RegisteredUserInline(admin.TabularInline):
    model = RegisterationEvents.user.through
    extra = 0
    can_delete = False
    verbose_name = "المسجل"
    verbose_name_plural = "المسجلين"
    readonly_fields = ['user_full_name', 'user_email', 'user_id_number', 'id_front_preview', 'id_back_preview']
    fields = readonly_fields

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.user.role in ['central_unit_head', 'unit_member']
            and request.user.central_unit
            and request.user.central_unit.name in ['المركز الاعلامي', 'لجنة البرمجة', 'وحدة التنظيم المركزي']
        )

    def has_change_permission(self, request, obj=None):
        return False  # Make inline read-only for non-superusers

    def user_full_name(self, obj):
        return obj.user.full_name

    def user_email(self, obj):
        return obj.user.email

    def user_id_number(self, obj):
        return obj.user.id_number

    def id_front_preview(self, obj):
        if obj.user.id_front:
            return format_html('<img src="{}" width="80"/>', obj.user.id_front.url)
        return "No Image"

    def id_back_preview(self, obj):
        if obj.user.id_back:
            return format_html('<img src="{}" width="80"/>', obj.user.id_back.url)
        return "No Image"

    


class RegisteredActivityUserInline(admin.TabularInline):
    model = RegisterationActivities.user.through
    extra = 0
    can_delete = False
    verbose_name = "Registered User"
    verbose_name_plural = "Registered Users"
    readonly_fields = ['user_full_name', 'user_email', 'user_id_number', 'id_front_preview', 'id_back_preview']
    fields = readonly_fields
    
    
    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        return (
            request.user.role in ['central_unit_head', 'unit_member']
            and request.user.central_unit
            and request.user.central_unit.name in ['المركز الاعلامي', 'لجنة البرمجة', 'وحدة التنظيم المركزي']
        )

    def has_change_permission(self, request, obj=None):
        return False

    def user_full_name(self, obj):
        return obj.user.full_name

    def user_email(self, obj):
        return obj.user.email

    def user_id_number(self, obj):
        return obj.user.id_number

    def id_front_preview(self, obj):
        if obj.user.id_front:
            return format_html('<img src="{}" width="80"/>', obj.user.id_front.url)
        return "No Image"

    def id_back_preview(self, obj):
        if obj.user.id_back:
            return format_html('<img src="{}" width="80"/>', obj.user.id_back.url)
        return "No Image"

class RegisterationEventsAdmin(admin.ModelAdmin):
    list_display = ['event', 'display_users_count'] 
    inlines = [RegisteredUserInline]
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return qs
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة':
            return qs
        return qs

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def has_module_permission(self, request):
        if request.user.is_authenticated:
            if request.user.role == 'unit_member' and request.user.central_unit =='وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة' :
                return True
            if request.user.is_superuser:
                return True
        

    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة'

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة'
        
    def display_users_count(self, obj):
        return obj.user.count()
    display_users_count.short_description = 'عدد المسجلين' 


class RegisterationActivitiesAdmin(admin.ModelAdmin):
    list_display = ['activities', 'display_users_count']
    inlines = [RegisteredActivityUserInline]
    
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return qs
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة':
            return qs
        return qs

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def has_module_permission(self, request):
        if request.user.is_authenticated:
            if request.user.role == 'unit_member' and request.user.central_unit =='وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة' :
                return True
            if request.user.is_superuser:
                return True
        

    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة'

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة'

    def display_users_count(self, obj):
        return obj.user.count()
    display_users_count.short_description = 'عدد المسجلين'

    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return qs
        if request.user.role == 'unit_member' and request.user.central_unit and (
            request.user.central_unit.name == 'وحدة التنظيم المركزي' or
            request.user.central_unit.name == 'لجنة البرمجة'
        ):
            return qs
        return qs.none()
    
    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي' or request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة'

    
    
admin.site.register(RegisterationActivities,RegisterationActivitiesAdmin)
admin.site.register(RegisterationEvents,RegisterationEventsAdmin)