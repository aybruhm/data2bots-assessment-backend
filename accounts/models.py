# Django Imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Native Imports
import uuid

# Own Imports
from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # unique ids
    id = models.BigAutoField(auto_created=True, primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, help_text="User unique ID.")
    
    # information (necessaries)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)

    # booleans
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname", "lastname", "username"]

    # set objects to UserManager
    objects = UserManager()

    class Meta:
        verbose_name_plural = "Users"
        db_table = "users" 
    
    def __str__(self) -> str:
        return self.email
    
    def fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"