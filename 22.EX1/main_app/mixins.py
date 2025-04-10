from django.db import models
from django.core.validators import MinLengthValidator


class NameMixin(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    class Meta:
        abstract = True


class BirthDateMixin(models.Model):
    birth_date = models.DateField(default='1900-01-01')

    class Meta:
        abstract = True


class NationalityMixin(models.Model):
    nationality = models.CharField(
        max_length=50,
        default='Unknown'
    )

    class Meta:
        abstract = True
