from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='avatars/', null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    year_of_experience = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0.0)
    address = models.CharField(max_length=255, blank=True, null=True)
    preferred_language = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name
