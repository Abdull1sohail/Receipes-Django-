from django.db import models

# Create your models here.

class Students(models.Model):
    Name = models.CharField(max_length=25)
    Age = models.IntegerField(null=True)
    Email = models.EmailField(null=True)
    Address = models.TextField(null=True)
    PhoneNumber = models.IntegerField(null=True)

class cars(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name 
