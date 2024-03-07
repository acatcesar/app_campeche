from django.db import models
from adm.models import Usuario, Apartamento


class Estadia(models.Model):
    hospedagem  = models.ForeignKey (Usuario, on_delete=models.PROTECT)
    apartamento = models.ForeignKey (Apartamento, on_delete=models.PROTECT)
    dataEntrada = models.DateField()
    dataSaida = models.DateField()
    qntDias = models.IntegerField()
    valor = models.DecimalField(max_digits = 5,decimal_places = 2)
