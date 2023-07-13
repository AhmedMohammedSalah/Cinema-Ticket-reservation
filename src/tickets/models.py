from django.db import models

# Create your models here.

#business model
# tickets guest , Movie , reservation 
class Movie(models.Model):
    hall= models.CharField(max_length=10)
    movie_name=models.CharField(max_length=10)
    date=models.DateField( auto_now=False, auto_now_add=False)
    
class Guest (models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    
    
class Reservation (models.Model):
    guest =models.ForeignKey(Guest, related_name="reservation", on_delete=models.CASCADE)
    movie =models.ForeignKey(Movie, related_name="reservation", on_delete=models.CASCADE)
    
    

