
from django.db import models



class TipuEleisaun(models.Model):
    tipu = models.CharField(max_length=500)

    def __str__(self):
        return self.tipu




class Eleisaun(models.Model):
    tinan = models.IntegerField()
    tipu_eleisaun = models.ForeignKey(TipuEleisaun, on_delete=models.SET_NULL, null=True, blank=True)
    ronda = models.CharField(max_length=50, null=True, blank=True)
    observasaun = models.CharField(max_length=255)
    total_eleitores = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "Eleisaun " + str(self.tipu_eleisaun.tipu) + " " + str(self.tinan) + " " + self.ronda



class SentruVotasaun(models.Model):
    # Eskolla ba Sentru Votasaun iha Liur ka Rai-Laran
    CHOICES = (('Natl', 'Nasionál'), ('Intl', 'Internasionál'),)

    fatin_votasaun = models.CharField(max_length=255)
    nivel = models.CharField(max_length=10, choices = CHOICES)

    def __str__(self):
        return self.fatin_votasaun




class Partidu(models.Model):
    sigla = models.CharField(max_length=25)
    naran = models.CharField(max_length=100)
    tinan = models.IntegerField()

    def __str__(self):
        return self.naran




class Kandidatu(models.Model):
    naran = models.CharField(max_length=100)
    afiliasaun_partidaria = models.ForeignKey(Partidu, on_delete=models.SET_NULL, null=True, blank=True)
    observasaun = models.CharField(max_length=255)
    numeru_sorteiu = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.naran





class Apuramentu(models.Model):
    kandidatu = models.ForeignKey(Kandidatu, on_delete=models.CASCADE)
    sentru_votasaun = models.ForeignKey(SentruVotasaun, on_delete=models.SET_NULL, null=True, blank=True)
    total_votu = models.IntegerField()
    eleisaun = models.ForeignKey(Eleisaun, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.kandidatu) + " nia votu iha " + str(self.sentru_votasaun) + " hamutuk " + str(self.total_votu) + " iha " + str(self.eleisaun)
