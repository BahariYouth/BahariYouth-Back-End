from django.contrib import admin
from accounts.models import User
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.contrib import admin

from rest_framework.authtoken.models import Token

class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user', 'created']
    
if not Token._meta.abstract:
    admin.site.register(Token, TokenAdmin)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_link', 'action_flag', 'change_message']
    list_filter = ['user', 'content_type', 'action_flag']
    search_fields = ['object_repr', 'change_message']

    def object_link(self, obj):
        if obj.content_type and obj.object_id:
            try:
                url = reverse(f'admin:{obj.content_type.app_label}_{obj.content_type.model}_change', args=[obj.object_id])
                return format_html('<a href="{}">{}</a>', url, obj.object_repr)
            except:
                return obj.object_repr
        return obj.object_repr

    object_link.short_description = 'Object'

admin.site.register(LogEntry, LogEntryAdmin)



class CustomUserAdmin(BaseUserAdmin):
    ordering = ['email'] 
    list_display = ['email', 'full_name', 'role', 'display_image']
    readonly_fields = ['display_image']

    fieldsets = (
        ('عام', {'fields': ('email', 'password')}),
        ('معلومات شخصية', {
            'fields': (
                'full_name',
                'role',
                'governorate',
                'central_unit',
                'image',
                'display_image'
            )
        }),
        ('الصلاحيات', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
        ('تواريخ', {'fields': ('last_login',)}),
    )

    # ✅ حل المشكلة: تعريف add_fieldsets يدويًا
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'role', 'governorate','central_unit', 'image'),
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        readonly = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return readonly + ['password']
        return readonly

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            # Remove password from editable fields for non-superusers
            new_fieldsets = []
            for name, opts in fieldsets:
                fields = [f for f in opts['fields'] if f != 'password']
                new_fieldsets.append((name, {'fields': fields}))
            return new_fieldsets
        return fieldsets

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="80" style="border-radius:50%;"/>', obj.image.build_url())
        return "لا توجد صورة"
    
    display_image.short_description = "الصورة"

admin.site.register(User, CustomUserAdmin)
