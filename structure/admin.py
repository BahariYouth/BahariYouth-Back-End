from django.contrib import admin
from .models import Governorate,CentralUnit
from django.contrib import admin
from django import forms
from accounts.models import User
from .forms import GovernorateForm,CentralUnitrateForm
    
class GovernorateAdmin(admin.ModelAdmin):
    list_display = ['name_ar','name_en' ,'address_ar','address_en', 'head','vice']
    search_fields = ['name_ar','head','vice']
    readonly_fields = ['latitude', 'longitude']
    form = GovernorateForm
    
    def has_module_permission(self, request):
        if request.user.is_superuser:
                return True

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
                return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
                return True
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
                return True
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        if request.user.is_superuser:
                return True
        return super().has_add_permission(request)

class CentralUnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'head', 'vice']
    search_fields = ['name', 'head', 'vice']
    form = CentralUnitrateForm

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser



admin.site.register(Governorate,GovernorateAdmin)

admin.site.register(CentralUnit,CentralUnitAdmin)
