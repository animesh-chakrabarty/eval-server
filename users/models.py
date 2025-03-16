from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email can't be empty")
        if not password:
            raise ValueError("Password can't be empty")
        email = self.normalize_email(email)        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('role', User.Role.ADMIN)
        extra_fields["is_active"] = True
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    class Role(models.IntegerChoices):
        ADMIN = 1, "Admin"
        HOST = 2, "Host"
        CANDIDATE = 3, "Candidate"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.IntegerField(
        choices= Role.choices,
        default=Role.CANDIDATE
    )
    is_active = models.BooleanField(default=False)
    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserOTPMapping(models.Model):
    userId = models.OneToOneField('users.User', on_delete=models.CASCADE)
    OTP = models.CharField(max_length=6)