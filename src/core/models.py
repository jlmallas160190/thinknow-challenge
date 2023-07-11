from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    MALE = "M"
    FEMALE = "F"
    SEX = (
        (MALE, "Masculino"),
        (FEMALE, "Femenino"),
    )
    nombre = models.CharField(_("Nombre"), max_length=30, blank=True)
    edad = models.IntegerField(_("Edad"), blank=True)
    sexo = models.CharField(
        _("sexo"),
        choices=SEX,
        max_length=10,
        default=MALE,
    )
    nacionalidad = models.CharField(_("Nacionalidad"), max_length=150, blank=True)
