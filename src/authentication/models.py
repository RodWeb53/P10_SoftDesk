from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **Kwargs):
        if not email:
            raise ValueError("Vous devez entrer un email")
        if not first_name:
            raise ValueError("Vous devez entrer un prénom")
        if not last_name:
            raise ValueError("Vous devez entrer un nom")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def has_perm(slf, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
