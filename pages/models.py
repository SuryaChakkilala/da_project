from django.db import models

# Create your models here.
class Facility(models.Model):
    type_choice = (
        ("Vehicle", "Vehicle"),
        ("Cargo", "Cargo"),
        ("Goods", "Goods")
    )

    name = models.CharField(max_length=255, blank=True, unique=True)
    address = models.TextField(blank=True, null=True)
    type = models.TextField(choices=type_choice)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Vehicle(models.Model):
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + str(self.time_added)
    
class Cargo(models.Model):
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + str(self.time_added)

class Goods(models.Model):
    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + str(self.time_added)