
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



class Tratta(models.Model):
    codice = models.CharField(max_length=50, default='', unique=True)
    aereo = models.ForeignKey(Aereo, on_delete=models.SET_NULL, null=True, blank=False)
    volo = 0
    ora_partenza = models.TimeField(default='')
    ora_arrivo = models.TimeField(default='')
    data_partenza = models.DateField(default='')
    data_arrivo = models.DateField(default='')
    aeroporto_partenza = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL, null=True, blank=False, related_name='aeroporto_partenza')
    aeroporto_arrivo = models.ForeignKey(Aeroporto, on_delete=models.SET_NULL, null=True, blank=False, related_name='aeroporto_arrivo')