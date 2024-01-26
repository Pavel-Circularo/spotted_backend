from django.db import models
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=30)
    year = models.IntegerField()
    picture = models.ImageField(upload_to='car_images')

    def __str__(self):
        return f"{self.brand.name} {self.model} - {self.year}"
