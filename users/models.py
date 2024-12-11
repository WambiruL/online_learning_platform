from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import viewsets
from django.contrib.auth.models import BaseUserManager

# Custom User model with roles
class UserManager(BaseUserManager):
    # Create a regular user
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    # Create a superuser with elevated permissions
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # Define user roles
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('approver', 'Approver'),
    )

    username = None  # Remove the default username field
    email = models.EmailField(unique=True)  # Email is the unique identifier
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)  # Assign roles

    # Unique related_name attributes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True
    )

    objects = UserManager()  # Use the custom user manager

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email  # String representation of the user
