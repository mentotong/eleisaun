from django.contrib import admin

from .models import (
    SentruVotasaun,
    TipuEleisaun,
    Kandidatu,
    Apuramentu,
    Partidu,
    Eleisaun,
)


admin.site.register(SentruVotasaun)
admin.site.register(TipuEleisaun)
admin.site.register(Kandidatu)
admin.site.register(Apuramentu)
admin.site.register(Partidu)
admin.site.register(Eleisaun)