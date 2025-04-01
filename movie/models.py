from django.db import models

class Movie(models.Model):
    """ Model from movies"""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    only_adult = models.BooleanField(default=False)
    cast = models.ManyToManyField('core.Actor', related_name='movie_cast_actors')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Listado de Peliculas'

    def __str__(self):
        return self.name
