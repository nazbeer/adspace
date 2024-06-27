from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.

# class Role(models.Model):
#     name = models.CharField(_('role name'), max_length=255, unique=True)
#     description = models.TextField(_('role description'), blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = _('role')
#         verbose_name_plural = _('roles')
#         ordering = ['name']

USER_CHOICES = [
        ('admin', 'Admin'),
        ('vendor', 'Vendor'),
        ('customer', 'Customer'),
        ('superuser', 'Superuser'),
        ]

STATUS_CHOICES = [

        ('active', 'Active'),
        ('inactive', 'Inactive'),

        ]

class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email address already exists."),
        },
    )
    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        _('first name'),
        max_length=255,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=255,
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=15,
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    role = models.CharField(_('user type'), max_length=20, choices=USER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']


# class Vendor(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(_('created at'), auto_now_add=True)
#     updated_on = models.DateTimeField(_('updated at'), auto_now=True)


#     class Meta:
#         verbose_name = 'vendor'
#         verbose_name_plural = 'vendors'
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.user.email
