from django.db import models
from django.conf import settings
from accounts.models import User
from events.models import Event
from activities.models import Activities


class RegisterationEvents(models.Model):
    user = models.ManyToManyField(
        User,
        verbose_name='مستخدم'
    )
    
    event = models.ForeignKey(
        Event,
        verbose_name='العاليات',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = 'تسجيلات العاليات'
        verbose_name_plural = 'تسجيلات الفعاليات'
    
    def __str__(self):
        return str(self.event)
    
class RegisterationActivities(models.Model):
    user = models.ManyToManyField(
        User,
        verbose_name='مستخدم',
    )
    
    activities = models.ForeignKey(
        Activities,
        verbose_name='النشاطات',
        on_delete=models.CASCADE,
    )
    
    class Meta:
        verbose_name = 'تسجيلات الانشطة'
        verbose_name_plural = 'تسجيلات الانشطة'
    
    def __str__(self):
        return str(self.activities)
    