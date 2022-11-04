from django.db import models

TIME_format = ['%I:%M %p',]

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=80)
    hours_of_operation_monday_open =  models.TimeField()
    hours_of_operation_monday_close = models.TimeField()
    hours_of_operation_tuesday_open = models.TimeField()
    hours_of_operation_tuesday_close = models.TimeField()
    hours_of_operation_wenesday_open = models.TimeField()
    hours_of_operation_wenesday_close = models.TimeField()
    hours_of_operation_thursday_open = models.TimeField()
    hours_of_operation_thursday_close = models.TimeField()
    hours_of_operation_friday_open = models.TimeField()
    hours_of_operation_friday_close = models.TimeField()
    hours_of_operation_saturday_open = models.TimeField()
    hours_of_operation_saturday_close = models.TimeField()
    hours_of_operation_sunday_open = models.TimeField()
    hours_of_operation_sunday_close = models.TimeField()
    
    # def __str__(self):
    #     return self.name
    



"""
# models.py
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
name and alias are character fields where we can store strings. The __str__ method just tells Django what to print when it needs to print out an instance of the Hero model."""