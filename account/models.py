from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    STATUC_CHOICES = (
        ('user', 'Пользователь'),
        ('assistant', 'Ассистент')
    )

    email = models.EmailField(_('email address'), unique=True)
    status = models.CharField(max_length=50, choices=STATUC_CHOICES, default='user', verbose_name='Статус аккаунта')
