from django.db import models

# Create your models here.
class livre(models.Model):
     titre = models.CharField(max_length=100)
     auteur = models.CharField(max_length=100)
     description = models.CharField(max_length=200,default="")
     image = models.ImageField(upload_to='images/')
     prix = models.IntegerField()
     disponible = models.BooleanField(default=True)
     isbn= models.CharField(max_length=11, default="0")
     def __str__(self):
         return self.titre
