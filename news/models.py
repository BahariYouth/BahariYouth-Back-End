from django.db import models
from django.conf import settings
from structure.models import Governorate
from events.models import Category
from cloudinary.models import CloudinaryField

class News(models.Model):
    title_ar = models.CharField(
        max_length=255,
        verbose_name="العنوان بالعربي"
    )
    title_en = models.CharField(
        max_length=255,
        verbose_name="العنوان بالإنجليزي"
    )
    description_ar = models.TextField(
        verbose_name="الوصف بالعربي"
    )
    description_en = models.TextField(
        verbose_name="الوصف بالإنجليزي"
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name="تاريخ الخبر"
    )
    governorate = models.ForeignKey(
        'structure.Governorate',
        on_delete=models.CASCADE,
        verbose_name="المحافظة"
    )
    category = models.ManyToManyField(
        'events.Category',
        verbose_name='الفئات',
    )
    created_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        related_name='created_news',
        verbose_name="تم الإنشاء بواسطة"
    )
    updated_by = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_news',
        verbose_name="تم التعديل بواسطة"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخر تعديل"
    )

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"

    def __str__(self):
        return self.title_ar



class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="الخبر"
    )
    image = CloudinaryField(
        verbose_name="صورة الخبر"
    )

    def __str__(self):
        return f"صورة لـ {self.news.title_ar}"

    class Meta:
        verbose_name = "صورة الخبر"
        verbose_name_plural = "صور الخبر"
