from django.db import models
from django.conf import settings

class Governorate(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='governorate_heads')
    vice = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='governorate_vices')
    longitude = models.DecimalField(max_digits=30, decimal_places=20)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='department_heads')
    vice = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='department_vices')
    governorate = models.ForeignKey(Governorate, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='branch_heads')
    vice = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='branch_vices')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
