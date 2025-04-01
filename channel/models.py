from django.db import models

class Channel(models.Model):
    """ Model from channels"""

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
    logo = models.ImageField(upload_to='channels/', blank=True, null=True)
    only_adult = models.CharField(max_length=200, blank=True, null=True, choices=AGE_PROGRAMS)
    main_category = models.ForeignKey('core.Category', on_delete=models.CASCADE, related_name='channel_main_category')
    other_categories = models.ManyToManyField('core.Category', related_name='channel_other_categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Listado de Canales'

    def __str__(self):
        return self.name