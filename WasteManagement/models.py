from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime

WASTE_TYPE = [('compost', 'compost'),
              ('recycle', 'recycle'), 
              ('trash', 'trash')]

FOOD_TYPE = [('meat', 'meat'),
             ('poletrie', 'poletrie'),
             ('vegetable', 'vegetable'),
             ('fruit', 'fruit'),
             ('dairy', 'dairy'),
             ('other', 'other')]

FRIGDE_LOC = [('fridge', 'less than 40'),
              ('freezer', '0')]

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'uploads/user_{instance.email}_{instance.username}/{filename}'


'''
# Create user
class User(models.Model):
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=50, null=False)
    photo = models.ImageField(upload_to=user_directory_path)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.username
'''

# Create your models here.
class Waste(models.Model):
    waste_id = models.AutoField(primary_key=True)
    waste_name = models.CharField(max_length=20, default='home')
    qty_recorded = models.PositiveIntegerField(default=0, null=False)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE, default='compost', null=False)
    date_recorded = models.DateField(default=timezone.now, null=False)
    description = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + '_' + self.waste_name


# Left over table
class Frigde(models.Model):
    fg_name = models.CharField(max_length=30, default='frigde_1', null=False)
    storage_date = models.DateField(default=timezone.now, null=False)
    storage_temp = models.CharField(max_length=30, choices=FRIGDE_LOC, default='fridge', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f'the fridge {self.fg_name} at {self.storage_date} degree'

class ItemOrFood(models.Model): 
    name = models.CharField(max_length=30, null=False)
    expiration_date = models.DateField(null=True)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE, default='other', null=False)
    item_description = models.CharField(max_length=30, null=True)
    qty = models.IntegerField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fridge = models.ForeignKey(Frigde, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} and the tyoe of {self.food_type}'

class ShoppingList(models.Model):
    shopping_date = models.DateField(default=timezone.now, null=True)
    budget = models.IntegerField(null=False, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = ArrayField(models.CharField(max_length=30), size=100, default=list, null=True)

    def __str__(self):
        return f'{self.shopping_date} by userId {self.user}'




