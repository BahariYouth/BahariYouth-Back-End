from django.db import models
from accounts.models import User
from events.models import Event,Category
from structure.models import Governorate
from django.conf import settings
from cloudinary.models import CloudinaryField




class Activities(models.Model):
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    
    title_ar = models.CharField(
        max_length=255,
        verbose_name='العنوان بالعربي'
    )
    title_en = models.CharField(
        max_length=255,
        verbose_name='العنوان بالانجليزي'
    )
    description_ar = models.TextField(
        verbose_name="الوصف بالعربي"
    )
    description_en = models.TextField(
        verbose_name="الوصف بالانجليزي"
    )
    address_ar = models.CharField(
        max_length=255,
        verbose_name="عنوان النشاط بالعربي"
    )
    address_en = models.CharField(
        max_length=255,
        verbose_name="عنوان النشاط بالانجليزي"
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
    category = models.ForeignKey (
        Category,
        on_delete=models.CASCADE,
        verbose_name ='الفئات',
    )
    is_private = models.BooleanField(default=False,verbose_name='طريقة التواصل')
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='offline',verbose_name='حالة النشاط')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_activities',
        verbose_name='تم الإنشاء بواسطة'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_activities',
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
        verbose_name='عدد الاماكن'
    )

    def __str__(self):
        return self.title_ar

    class Meta:
        verbose_name = "النشاطات"
        verbose_name_plural = "النشاطات"