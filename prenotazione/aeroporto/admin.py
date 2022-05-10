from django.contrib import admin

from aeroporto.models import Aereo, Aeroporto, Tratta

# Register your models here.
class AereoAdmin(admin.ModelAdmin):
    list_display = ('codice', 'modello', 'miglie_max', 'posti')
    list_filter = ('codice', 'modello', 'miglie_max', 'posti')

admin.site.register(Aereo, AereoAdmin)



class AeroportoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codice_iata', 'lat_lng')
    list_filter = ('nome', 'codice_iata', 'lat_lng')

admin.site.register(Aeroporto, AeroportoAdmin)


class TrattaAdmin(admin.ModelAdmin):
    list_display = ('aeroporto_partenza', 'aeroporto_arrivo', 'ora_partenza', 'data_partenza')
    list_filter = ('aeroporto_partenza', 'aeroporto_arrivo', 'ora_partenza', 'data_partenza')

admin.site.register(Tratta)