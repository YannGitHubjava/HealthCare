from django.db import models

# Create your models here.
class User(models.Model):
    firtName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    def _str_(self):
        return self.firtName + ' ' + self.lastName

class Patient(models.Model):
    firtName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    def _str_(self):
        return self.firtName + ' ' + self.lastName