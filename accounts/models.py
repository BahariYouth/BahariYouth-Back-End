from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from structure.models import Governorate,Department,Branch


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email")
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
    """
    one user model with different roles as a user as default
    
    """
    
    ROLE_CHOICES = [
        ('user', 'User'),
        ('country_head', 'Country Head'),
        ('country_hand', 'Country Hand'),
        ('governorate_head', 'Governorate Head'),
        ('governorate_hand', 'Governorate Hand'),
        ('department_head', 'Department Head'),
        ('department_hand', 'Department Hand'),
        ('branch_head', 'Branch Head'),
        ('branch_hand', 'Branch Hand'),
        ('branch_member','Member')
    ]

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    governorate = models.ForeignKey(Governorate, null=True, blank=True, on_delete=models.SET_NULL, related_name="users_in_governorate")
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL, related_name="users_in_department")
    branch = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.SET_NULL, related_name="users_in_branch")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name

