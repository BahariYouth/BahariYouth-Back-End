from django.db import models
from django.conf import settings
from structure.models import Governorate
from cloudinary.models import CloudinaryField





class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='الفئات'
    )
    
    class Meta:
        verbose_name = 'فئة'
        verbose_name_plural = 'فئات'
    
    def __str__(self):
        return self.name
        

class Event(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    title_ar = models.CharField(
        max_length=255,
        verbose_name='العنوان بالعربي'
    )
    title_en = models.CharField(
        max_length=255,
        verbose_name='العنوان بالإنجليزي'
    )
    description_ar = models.TextField(
        verbose_name="الوصف بالعربي"
    )
    description_en = models.TextField(
        verbose_name="الوصف بالإنجليزي"
    )
    address_ar = models.CharField(
        max_length=255,
        verbose_name="عنوان الفعالية بالعربي"
    )
    address_en = models.CharField(
        max_length=255,
        verbose_name="عنوان الفعالية بالإنجليزي"
    )
    date = models.DateTimeField(
        verbose_name="تاريخ الفعالية"
    )
    image = CloudinaryField(
        verbose_name='صورة الفعالية',
        blank=True,
        null=True
    )
    governorate = models.ForeignKey(
        Governorate,
        on_delete=models.CASCADE,
        verbose_name='المحافظة'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='الفئات'
    )
    is_private = models.BooleanField(default=False, verbose_name='طريقة التواصل')
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='offline',
        verbose_name='حالة الفعالية'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_events',
        verbose_name='تم الإنشاء بواسطة'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_events',
        verbose_name='تم التعديل بواسطة'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاريخ الإنشاء'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='آخر تعديل'
    )
    tickets = models.IntegerField(
        verbose_name='عدد الأماكن'
    )

    def __str__(self):
        return self.title_ar

    class Meta:
        verbose_name = "فعالية"
        verbose_name_plural = "الفعاليات"
