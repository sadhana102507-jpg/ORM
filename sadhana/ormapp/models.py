from django.db import models
from django.contrib import admin
class Car(models.Model):
    mid=models.IntegerField()
    brand=models.CharField(max_length=100)
    collection=models.IntegerField()
    price=models.IntegerField()
    rating=models.FloatField()

class CarAdmin(admin.ModelAdmin):
    list_display=('mid','brand','collection','price','rating')


