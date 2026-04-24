from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model with additional fields
    """
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField(_('biography'), max_length=500, blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', blank=True, null=True)
    website = models.URLField(_('website'), blank=True)
    telegram = models.CharField(_('telegram'), max_length=100, blank=True)
    github = models.CharField(_('github'), max_length=100, blank=True)

    # Additional fields
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    location = models.CharField(_('location'), max_length=100, blank=True)

    # Timestamps
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    # Email verification
    email_verified = models.BooleanField(_('email verified'), default=False)
    email_verification_token = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username

    @property
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return f'https://ui-avatars.com/api/?name={self.username}&background=random'
