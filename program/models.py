from django.db import models

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

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='programs/', blank=True, null=True)
    only_adult = models.CharField(max_length=200, blank=True, null=True, choices=AGE_PROGRAMS)
    main_category = models.ForeignKey('core.Category', on_delete=models.CASCADE, related_name='program_main_category')
    other_categories = models.ManyToManyField('core.Category', related_name='program_other_categories')
    actors = models.ManyToManyField('core.Actor', related_name='actors')
    release_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Listado de Programas'

    def __str__(self):
        return self.name
    

class Episodes(models.Model):
    """ Model from episodes"""

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='episodes/', blank=True, null=True)
    duration = models.IntegerField()
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='program')
    cast = models.ManyToManyField('core.Actor', related_name='cast_actors')
    release_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Episodio'
        verbose_name_plural = 'Listado de Episodios'

    def __str__(self):
        return self.name
