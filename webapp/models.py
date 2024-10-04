from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    fecha_de_nacimiento = models.DateField(null=True, blank=True)


class Bautizo(models.Model):
    parroquia = models.CharField(max_length=255, default="'La Purisima' - Concepción")
    libro = models.PositiveIntegerField()
    fojas = models.PositiveIntegerField()
    numero = models.PositiveIntegerField()
    apellidos = models.CharField(max_length=50)
    nombres = models.CharField(max_length=30)
    lugar_nacimiento = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_bautizo = models.DateField(null=True, blank=True)
    padre = models.CharField(max_length=80)
    nacimientolugarpadre = models.CharField(max_length=50, null=True, blank=True)
    madre = models.CharField(max_length=80)
    nacimientolugarmadre = models.CharField(max_length=50, null=True, blank=True)
    padrinos = models.CharField(max_length=150, null=True, blank=True)
    oficiante = models.CharField(max_length=255)
    anotaciones = models.CharField(max_length=255, default="Ninguno")


class Matrimonio(models.Model):
    parroquia = models.CharField(max_length=255, default="'La Purisima' - Concepción")
    libro = models.PositiveIntegerField()
    fojas = models.PositiveIntegerField()
    numero = models.PositiveIntegerField()
    esposo = models.CharField(max_length=80)
    lugar_bautizo_esposo = models.CharField(max_length=80)
    esposa = models.CharField(max_length=80)
    lugar_bautizo_esposa = models.CharField(max_length=80)
    padre_esposo = models.CharField(max_length=80)
    madre_esposo = models.CharField(max_length=80)
    padre_esposa = models.CharField(max_length=80)
    madre_esposa = models.CharField(max_length=80)
    padrinos = models.CharField(max_length=150, null=True, blank=True)
    fecha_matrimonio = models.DateField()
    anotaciones = models.CharField(max_length=255, default="Ninguno")


class Confirmacion(models.Model):
    nombre = models.CharField(max_length=80)
    ex_monsenor = models.CharField(max_length=80)
    parroquia = models.CharField(max_length=255, default="'La Purisima' - Concepción")
    fecha = models.DateField()
    padres = models.CharField(max_length=150)
    padrinos = models.CharField(max_length=150, null=True, blank=True)


class priComunion(models.Model):
    nombre = models.CharField(max_length=80)
    parroquia = models.CharField(max_length=255, default="'La Purisima' - Concepción")
    fecha = models.DateField()
    padre = models.CharField(max_length=80)
    madre = models.CharField(max_length=80)