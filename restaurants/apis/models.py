from django.db import models
from django import forms

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=80)
    hours_of_operation_monday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_monday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_monday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_monday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_monday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_monday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_monday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_monday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_tuesday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_tuesday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_tuesday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_tuesday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_tuesday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_tuesday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_tuesday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_tuesday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_wenesday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_wenesday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_wenesday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_wenesday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_wenesday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_wenesday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_wenesday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_wenesday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_thursday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_thursday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_thursday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_thursday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_thursday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_thursday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_thursday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_thursday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_friday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_friday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_friday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_friday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_friday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_friday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_friday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_friday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_saturday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_saturday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_saturday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_saturday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_saturday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_saturday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_saturday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_saturday_close_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_sunday_open_hour =  models.IntegerField(null=True)
    hours_of_operation_sunday_open_minutes = models.IntegerField(null=True)
    hours_of_operation_sunday_open_am_pm =  models.CharField(max_length=100)
    hours_of_operation_sunday_open_time =  models.TimeField(null=True, blank=True)
    hours_of_operation_sunday_close_hour =  models.IntegerField(null=True)
    hours_of_operation_sunday_close_minutes = models.IntegerField(null=True)
    hours_of_operation_sunday_close_am_pm =  models.CharField(max_length=100)
    hours_of_operation_sunday_close_time =  models.TimeField(null=True, blank=True)

    # hours_of_operation_monday_open =  models.CharField(null=True,max_length=50)
    # hours_of_operation_monday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_tuesday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_tuesday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_wenesday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_wenesday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_thursday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_thursday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_friday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_friday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_saturday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_saturday_close = models.CharField(null=True,max_length=50)
    # hours_of_operation_sunday_open = models.CharField(null=True,max_length=50)
    # hours_of_operation_sunday_close = models.CharField(null=True,max_length=50)
    # restaurants = models.Manager()
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