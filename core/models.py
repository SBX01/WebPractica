from django.db import models

# Create your models here.
class TipoServicio(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):

        return self.tipo
        

class Servicio(models.Model): 
   
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre
        
class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField(verbose_name="Correo")
    fecha = models.DateField()
    servi = models.ForeignKey(Servicio,on_delete=models.CASCADE, verbose_name="Servicio")
    tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo")
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    nombre = models.CharField(max_length=50)
    comentario =  models.CharField(max_length=50)
    nota =  models.IntegerField()

    def __str__(self):
        return self.nombre

class BlogPost(models.Model):
    titulo = models.CharField(max_length=50)
    post =  models.CharField(max_length=900)
    fechaPost =  models.DateField()
    imagenPost =  models.ImageField()
    
    def __str__(self):
        return self.titulo