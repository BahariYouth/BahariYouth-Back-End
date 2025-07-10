from django.db import models
from django.conf import settings
import re

class Governorate(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم المحافظة"
    )
    address = models.TextField(
        verbose_name="العنوان"
    )
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='governorate_heads',
        verbose_name="رئيس المحافظة"
    )
    vice = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='governorate_vices',
        verbose_name="نائب الرئيس"
    )
    location_link = models.URLField(
        blank=True,
        null=True,
        verbose_name="رابط الموقع",
        help_text="الصق رابط خرائط جوجل مثل: https://www.google.com/maps/place/.../@30.12345,31.67890,17z"
    )
    latitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="خط العرض"
    )
    longitude = models.FloatField(
        blank=True,
        null=True,
        verbose_name="خط الطول"
    )

    def save(self, *args, **kwargs):
        self.latitude = None
        self.longitude = None

        if self.location_link:
            match = re.search(r"@(-?\d+\.\d+),(-?\d+\.\d+)", self.location_link)
            if match:
                try:
                    self.latitude = float(match.group(1))
                    self.longitude = float(match.group(2))
                except Exception:
                    self.latitude = None
                    self.longitude = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محافظة"
        verbose_name_plural = "المحافظات"


class CentralUnit(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="اسم الوحدة"
    )
    head = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="central_head_of",
        verbose_name="رئيس الوحدة"
    )
    vice = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="central_deputy_of",
        verbose_name="نائب الرئيس"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "وحدة مركزية"
        verbose_name_plural = "الوحدات المركزية"
