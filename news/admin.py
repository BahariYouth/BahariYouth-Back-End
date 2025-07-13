from django.contrib import admin
from .models import News,NewsImage
from django.utils.html import format_html



class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 1
    min_num = 1

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        if request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)
    
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageInline]
    list_display = ['title', 'governorate', 'date', 'created_by']
    readonly_fields = ['created_by', 'updated_by','updated_at','created_at','date']
    
    fieldsets = (
        ('عام', {'fields': ('title', 'description','date','governorate')}),
        ('معلومات', {
            'fields': (
                'created_at',
                'created_by',
                'updated_at',
                'updated_by'
            )
        }),
    )
    
    
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return qs
        return qs.filter(created_by=request.user)


    def has_module_permission(self, request):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي'

    def has_view_permission(self, request, obj=None):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        return request.user.role == 'unit_member' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي'

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        if obj and obj.created_by != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
            return True
        if obj and obj.created_by != request.user:
            return False
        return True
    
    def has_add_permission(self, request):
        if request.user.is_authenticated:
            if request.user.is_authenticated:
                if request.user.role == 'unit_member' and request.user.central_unit.name =='المركز الاعلامي' :
                    return True
                if request.user.role == 'central_unit_head' and request.user.central_unit and request.user.central_unit.name == 'المركز الاعلامي':
                    return True
        return super().has_add_permission(request)

admin.site.register(News, NewsAdmin)
