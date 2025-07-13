from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from cloudinary.models import CloudinaryField
from structure.models import Governorate,CentralUnit

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("البريد الإلكتروني مطلوب")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('central_unit_head', 'رئيس وحدة مركزية'),
        ('central_unit_vice', 'نائب رئيس وحدة مركزية'),
        ('governorate_head', 'منسق محافظة'),
        ('governorate_vice', 'نائب منسق محافظة'),
        ('unit_member', 'عضو وحدة'),
    ]

    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    full_name = models.CharField(max_length=255, verbose_name="الاسم الكامل")
    image = CloudinaryField(blank=True, null=True,verbose_name="الصورة")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, verbose_name="الدور")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    central_unit = models.ForeignKey(CentralUnit, null=True, blank=True, on_delete=models.SET_NULL, related_name='centeralunit',verbose_name="الوحدة المركزية")
    governorate = models.ForeignKey(Governorate, null=True, blank=True, on_delete=models.SET_NULL, related_name='governrate',verbose_name="المحافظة")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستحدمين"
