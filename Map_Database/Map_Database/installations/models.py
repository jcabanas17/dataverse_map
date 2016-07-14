from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from decimal import Decimal

# Create your models here.
@python_2_unicode_compatible
class installation(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.0000'))
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.0000'))
    def __str__(self):
        return self.name
    pass

@python_2_unicode_compatible    
class institution(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default=Decimal('0.0000'))
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=True, default=Decimal('0.0000'))
    host = models.ForeignKey(
        'installation',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name