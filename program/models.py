from django.db import models
from channel.models import Channel

class Program(models.Model):
    """ Model from programs"""

    AGE_PROGRAMS = (
        ('I', 'Infantil'),
        ('A', 'Todo público'),
        ('7', 'Mayores de 7 años'),
        ('12', 'Mayores de 12 años'),
        ('15', 'Mayores de 15 años'),
        ('18', 'Mayores de 18 años'),
        ('X', 'Solo adultos'),
    )

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    image = models.ImageField(upload_to='programs/', verbose_name="Cartel", blank=True, null=True)
    age = models.CharField(max_length=200, verbose_name="Solo adultos", blank=True, null=True, choices=AGE_PROGRAMS)
    main_category = models.ForeignKey('core.Category', verbose_name="Categoría principal", on_delete=models.CASCADE, related_name='program_main_category')
    other_categories = models.ManyToManyField('core.Category', verbose_name="Otras categorías", related_name='program_other_categories')
    actors = models.ManyToManyField('core.Actor', verbose_name="Reparto", related_name='actors')
    release_date = models.DateField(blank=True, verbose_name="Estreno", null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, verbose_name="Canal")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Listado de Programas'

    def __str__(self):
        return self.name
    
class Season(models.Model):
    """ Model from seasons"""

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    image = models.ImageField(upload_to='seasons/', verbose_name="Cartel", blank=True, null=True)
    program = models.ForeignKey('Program', verbose_name="Programa", on_delete=models.CASCADE, related_name='season_program')
    release_date = models.DateField(blank=True, verbose_name="Estreno", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Temporada'
        verbose_name_plural = 'Listado de Temporadas'

    def __str__(self):
        return self.name
    

class Episodes(models.Model):
    """ Model from episodes"""

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    image = models.ImageField(upload_to='episodes/', verbose_name="Imagen", blank=True, null=True)
    duration = models.IntegerField(verbose_name="Duración", blank=True, null=True)
    program = models.ForeignKey('Program', verbose_name="Programa", on_delete=models.CASCADE, related_name='program')
    season = models.ForeignKey('Season', verbose_name="Temporada", on_delete=models.CASCADE, related_name='season', blank=True, null=True)
    cast = models.ManyToManyField('core.Actor', verbose_name="Reparto", related_name='cast_actors')
    release_date = models.DateField(blank=True, verbose_name="Estreno", null=True)
    link = models.URLField(verbose_name="Enlace media", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Listado de Episodios'

    def __str__(self):
        return self.name
