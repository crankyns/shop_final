from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import re



@deconstructible
class _PhoneValidator:

    _pattern = re.compile(
    "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
    )

    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError('Введите существующий мобильный номер.')


class CustomUser(AbstractUser):

    phone_number = models.CharField(
        max_length=20,
        validators=[_PhoneValidator()],
        verbose_name="Номер телефона"
        )
    
    coop_name = models.CharField(
        max_length=50,
        verbose_name="Наименование организации",
        blank=True, null=True)


    def __str__(self):
        return self.username

    class Meta:
        
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'