from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.db import models
from django.utils import timezone

from product_card.models import Book


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    username = models.ForeignKey("AppUser", on_delete=models.CASCADE, related_name="user_name")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created_date"]


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        unique=True,
        max_length=30,
    )

    email = models.EmailField()
    index = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.IntegerField(help_text="Enter the number in international format.", null=True)
    country = models.CharField(null=True, max_length=30)
    city = models.CharField(null=True, max_length=30)
    address = models.CharField(null=True, max_length=60)
    reserve_address = models.CharField(blank=True, null=True, max_length=60)
    additional_info = models.CharField(blank=True, null=True, max_length=150)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "username"
        verbose_name_plural = "usernames"
        abstract = False
