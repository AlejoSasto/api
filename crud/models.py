from django.db import models


# Create your models here.
class Project(models.Model):
    id_marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    activo = models.CharField(max_length=200)
    item_ya_usado = models.CharField(max_length=200)

    def __srt__(self):
        texto = "{0}({1})"
        return texto.format(self.id_marca, self.nombre, self.activo, self.item_ya_usado)
