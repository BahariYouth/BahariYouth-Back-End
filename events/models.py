from django.db import models
from django.conf import settings
from structure.models import Governorate
from cloudinary.models import CloudinaryField

class Event(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='العنوان'
    )
    description = models.TextField(
        verbose_name="الوصف"
    )
    date = models.DateTimeField(
        auto_now=True,
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "فعالية"
        verbose_name_plural = "الفعاليات"
