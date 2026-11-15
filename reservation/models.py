from django.db import models

# Create your models here.
class Booking(models.Model):

    name= models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    turf=models.PositiveIntegerField()
    match_date = models.DateField()
    duration = models.PositiveIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,null=True)
