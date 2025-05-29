from django.db import models

class Channel(models.Model):
    """ Model from channels"""

    AGE_PROGRAMS = (
        ('I', 'Infantil'),
        ('A', 'Todo público'),
        ('7', 'Mayores de 7 años'),
        ('12', 'Mayores de 12 años'),
        ('16', 'Mayores de 16 años'),
        ('18', 'Mayores de 18 años'),
        ('X', 'Solo adultos'),
    )

    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción", null=True)
    logo = models.ImageField(upload_to='channels/', verbose_name="Logo", blank=True, null=True)
    age = models.CharField(max_length=200, verbose_name="Solo adultos", blank=True, null=True, choices=AGE_PROGRAMS)
    main_category = models.ForeignKey('core.Category', verbose_name="Categoría principal", on_delete=models.CASCADE, related_name='channel_main_category')
    other_categories = models.ManyToManyField('core.Category', verbose_name="Otras categorías", related_name='channel_other_categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Listado de Canales'

    def __str__(self):
        return self.name