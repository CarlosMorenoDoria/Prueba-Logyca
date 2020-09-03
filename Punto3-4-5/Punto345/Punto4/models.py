from django.db import models

# Create your models here.
class tabla_numerosprimos(models.Model):

    key = models.IntegerField()
    primo = models.IntegerField() 




class tabla_primosgemelos(models.Model):

    key = models.IntegerField()
    gemelos=models.CharField(max_length=20)
    verificarconsulta=models.IntegerField(default=0)

