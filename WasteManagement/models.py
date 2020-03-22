from django.db import models
from django.utils import timezone
from datetime import datetime

WASTE_TYPE = [('compost', 'compost'),
              ('recycle', 'recycle'), 
              ('trash', 'trash')]

# Create your models here.
class Waste(models.Model):
    waste_id = models.PositiveIntegerField(primary_key=True)
    waste_name = models.CharField(max_length=20, default='home')
    qty_recorded = models.PositiveIntegerField(default=0, null=False)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE, default='compost', null=False)
    date_recorded = models.DateField(default=timezone.now, null=False)
    description = models.CharField(max_length=30, null=True)
    def _repr_(self):
        return self.waste_name + '_' + self.waste_name

