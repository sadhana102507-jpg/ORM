# Ex02 Django ORM Web Application
## Date: 19/09/2025

## AIM
To develop a Django application to store and retrieve data from car inventory database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py


from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

models.py


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
~~~





## OUTPUT
![alt text](<Screenshots/Screenshot (3).png>)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
