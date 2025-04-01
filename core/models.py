from django.db import models

class Category(models.Model):
    """ Model from categories"""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    only_adult = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='categories/', blank=True, null=True)


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
    )

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='actors/', blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=200, blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    genre = models.CharField(max_length=200, blank=True, null=True, choices=GENRE)
    only_adult = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Listado de Actores'

    def __str__(self):
        return self.name