from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos_equipos/')

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    equipo  = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='archivos_jugadores/')
    identificacion_pdf = models.FileField(upload_to='archivos_jugadores/')

    def __str__(self):
        return f'{self.nombre} - {self.equipo.nombre}'

    def delete(self, *args, **kwargs):
        if self.foto:
            self.foto.delete()
        if self.identificacion_pdf:
            self.identificacion_pdf.delete()

        super().delete(*args, **kwargs)