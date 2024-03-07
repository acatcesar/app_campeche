from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser


ESTADOS_CHOICES = (
    ("AC", "AC"),
    ("AL", "AL"),
    ("AP", "AP"),
    ("AM", "AM"),
    ("BA", "BA"),
    ("CE", "CE"),
    ("DF", "DF"),
    ("ES", "ES"),
    ("GO", "GO"),
    ("MA", "MA"),
    ("MT", "MT"),
    ("MS", "MS"),
    ("MG", "MG"),
    ("PA", "PA"),
    ("PB", "PB"),
    ("PR", "PR"),
    ("PE", "PE"),
    ("PI", "PI"),
    ("RJ", "RJ"),
    ("RN", "RN"),
    ("RS", "RS"),
    ("RO", "RO"),
    ("RR", "RR"),
    ("SC", "SC"),
    ("SP", "SP"),
    ("SE", "SE"),
    ("TO", "TO"),
)

class Apartamento(models.Model):
    nome = models.CharField(max_length=40)
    valor = models.DecimalField()
    numero = models.ImageField()
    status = models.BooleanField()



class Hospede(models.Model):
    celular = PhoneField(blank=True, help_text='Contact phone number')
    endereco = models.CharField(max_length=40)
    CEP = models.CharField(max_length=20)
    estado = models.CharField (max_length=40, choices=ESTADOS_CHOICES)


class Usuario(AbstractUser):
    apartamento_vistos = models.ManyToManyField("Apartamento")