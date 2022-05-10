
from django.db import models


# Create your models here.
class Aereo(models.Model):
    codice = models.CharField(max_length=50, default='', unique=True)
    modello = models.CharField(max_length=20, default='')
    miglie_max = models.IntegerField(default=0)
    posti = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.modello
    
    class Meta:
        verbose_name = 'Aereo'
        verbose_name_plural = 'Aerei'


class Aeroporto(models.Model):
    nome = models.CharField(max_length=50, default='')
    codice_iata = models.CharField(max_length=50, default='', unique=True)
    lat_lng = models.CharField(max_length=50, default='')

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Aeroporto'
        verbose_name_plural = 'Aeroporti'



class Tratta(models.Model):
    codice = models.CharField(max_length=50, default='', unique=True)
    ora_partenza = models.TimeField()
    ora_arrivo = models.TimeField()
    data_partenza = models.DateField()
    data_arrivo = models.DateField()
    aereo = models.ForeignKey(Aereo, on_delete=models.SET_NULL, null=True, blank=False)
    aeroporto_partenza = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL, null=True, blank=False, related_name='aeroporto_partenza')
    aeroporto_arrivo = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL, null=True, blank=False, related_name='aeroporto_arrivo')
    aereo = models.ForeignKey(Aereo, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self) -> str:
        return self.aeroporto_partenza + ' - ' + self.aeroporto_arrivo
    
    class Meta:
        verbose_name = 'Tratta'
        verbose_name_plural = 'Tratte'