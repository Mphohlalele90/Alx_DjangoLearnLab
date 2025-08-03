from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        user = super().create_user(username, email=email, password=password, **extra_fields)
        user.date_of_birth = date_of_birth
        user.profile_photo = profile_photo
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        user = super().create_superuser(username, email=email, password=password, **extra_fields)
        user.date_of_birth = date_of_birth
        user.profile_photo = profile_photo
        user.save(using=self._db)
        return user

#class CustomUser(AbstractUser):
#    date_of_birth = models.DateField(blank=True, null=True)
#    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

#    objects = CustomUserManager()