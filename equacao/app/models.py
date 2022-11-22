from django.db import models

# Create your models here.
class User(models.Model):
    
    a = models.IntegerField("A")
    
    b = models.IntegerField("B")
    
    c = models.IntegerField("C")
    raiz1=0
    raiz2=0
    
    def __str__(self):
        return f"Coeficiente A: {self.a}, Coeficiente B: {self.b}, Coeficiente C: {self.c}"
