from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

approval_status = (
              ('Approved', _('Approved')),
              ('Not Approved', _('Not Approved'))
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.IntegerField(unique=True, default=9999999999)
    manager_id = models.ForeignKey("self", on_delete=models.CASCADE, null=True, limit_choices_to={'is_staff': True})
    status = models.CharField(max_length=20, default="Not Approved", choices=approval_status)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Leads(models.Model):

    STATUS = (('hot', _('hot')),
              ('cold', _('cold')),
              ('med', _('med')),
              ('sold', _('sold'))
              )

    created_at = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_no = models.IntegerField(unique=True, default=9999999999)
    status = models.CharField(
        max_length=32,
        choices=STATUS
    )
    sales_representative = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_staff': False})

    def __str__(self):
        return self.email
