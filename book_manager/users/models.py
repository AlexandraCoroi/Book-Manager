import secrets
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import AuthUserManager
from .utils.constants import ACTIVATION_AVAILABILITY
from django.conf import settings

class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )
    password = models.CharField(_('password'), max_length=128, null=True, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()

# AuthUserModel = get_user_model()

AVAILABILITY = {
    ACTIVATION_AVAILABILITY['unit']: ACTIVATION_AVAILABILITY['value']
}

class Activation(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='activation'
    )
    token = models.CharField(
        max_length=64,
        default=secrets.token_hex(32)
    )
    expires_at = models.DateTimeField()
    activated_at = models.DateTimeField(default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.expires_at = timezone.now() + timezone.timedelta(days=2)
        super().save(*args, **kwargs)

    def is_token_valid(self):
        return (
            self.activated_at is None and
            timezone.now() < self.expires_at
        )