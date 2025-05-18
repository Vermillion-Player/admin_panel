from django.db import models
from channel.models import Channel

class Movie(models.Model):
    """ Model from movies"""

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    image = models.ImageField(upload_to='movies/', verbose_name="Cartel", blank=True, null=True)
    duration = models.IntegerField(blank=True, verbose_name="Duración", null=True)
    release_date = models.DateField(blank=True, verbose_name="Fecha de estreno", null=True)
    only_adult = models.BooleanField(default=False, verbose_name="Solo adultos")
    cast = models.ManyToManyField('core.Actor', verbose_name="Reparto", related_name='movie_cast_actors')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name="Canal")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Listado de Peliculas'

    def __str__(self):
        return self.name
