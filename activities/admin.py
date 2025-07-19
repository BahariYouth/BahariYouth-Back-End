from django.contrib import admin
from .models import Activities

class ActivitiestAdmin(admin.ModelAdmin):
    list_display = ['title_ar','title_en',"address_ar",'address_en', 'governorate', 'date', 'created_by']
    readonly_fields = ['created_by', 'updated_by','updated_at','created_at']

    fieldsets = (
        ('عام', {'fields': ('title_ar','title_en' ,'description_ar','description_en','category','tickets','address_ar','address_en','image','date','governorate')}),
        ('معلومات', {
            'fields': (
                'created_at',
                'created_by',
                'updated_at',
                'updated_by'
            )
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return qs
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة':
            return qs
        return qs.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return (request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي') or \
               (request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة')

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        return (request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي') or \
               (request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.is_authenticated:
            if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
                return False
            if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
                return True
        return False 

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
            return True
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'لجنة البرمجة':
            return True
        if obj and obj.created_by == request.user:
             return True
        return False


    def has_add_permission(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
                return True
            if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'وحدة التنظيم المركزي':
                return True
        return False 
    
admin.site.register(Activities, ActivitiestAdmin)