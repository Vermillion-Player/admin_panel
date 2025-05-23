from django.db import models

class Category(models.Model):
    """ Model from categories"""

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    only_adult = models.BooleanField(default=False, verbose_name="Solo adultos")
    logo = models.ImageField(upload_to='categories/', verbose_name="Logo", blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Listado de Categorías'

    def __str__(self):
        return self.name
    
    
class Actor(models.Model):
    """ Model from actors"""

    GENRE = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('T', 'Transgénero'),
        ('NB', 'No Binario'),
        ('O', 'Otro')
    )

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    image = models.ImageField(upload_to='actors/', verbose_name="Foto", blank=True, null=True)
    birthdate = models.DateField(blank=True, verbose_name="Fecha de nacimiento", null=True)
    birthplace = models.CharField(max_length=200, verbose_name="Origen", blank=True, null=True)
    height = models.FloatField(blank=True, verbose_name="Altura", null=True)
    weight = models.FloatField(blank=True, verbose_name="Peso", null=True)
    genre = models.CharField(max_length=200, verbose_name="Género", blank=True, null=True, choices=GENRE)
    only_adult = models.BooleanField(default=False, verbose_name="Solo adultos")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Listado de Actores'

    def __str__(self):
        return self.name