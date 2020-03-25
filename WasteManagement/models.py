from django.db import models
from django.utils import timezone
from datetime import datetime

WASTE_TYPE = [('compost', 'compost'),
              ('recycle', 'recycle'), 
              ('trash', 'trash')]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


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

# Create user
class WastUser(models.Model):
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    photo = models.ImageFile(upload_to=user_directory_path)
    password = models.CharField(max_length=50, null=False)

# Left over table
class LeftOver(models.Model):
    food_name = 
    food_type =
    food_cooked_date =
    item_age = 
    item_description = 
    
class ItemOrFood(models.Model):
    name = 
    description = 
    expiration =
    qty =

class ShoppingList():
    date_of_shoping = 
    money_spent = 

