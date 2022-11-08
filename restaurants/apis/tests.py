import datetime
from django.test import TestCase

from django.test import TestCase
from .models import Restaurant

class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(restaurant_name="thetest",
        hours_of_operation_monday_open_hour = 1,hours_of_operation_monday_open_minutes = 30,hours_of_operation_monday_open_am_pm = "AM" ,hours_of_operation_monday_open_time = datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_monday_close_hour = 12,hours_of_operation_monday_close_minutes = 0,hours_of_operation_monday_close_am_pm = "PM",hours_of_operation_monday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_tuesday_open_hour = 1,hours_of_operation_tuesday_open_minutes = 30,hours_of_operation_tuesday_open_am_pm = "AM",hours_of_operation_tuesday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_tuesday_close_hour = 12,hours_of_operation_tuesday_close_minutes = 0,hours_of_operation_tuesday_close_am_pm = "PM",hours_of_operation_tuesday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_wenesday_open_hour = 1,hours_of_operation_wenesday_open_minutes = 30,hours_of_operation_wenesday_open_am_pm = "AM",hours_of_operation_wenesday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_wenesday_close_hour = 12,hours_of_operation_wenesday_close_minutes = 0,hours_of_operation_wenesday_close_am_pm = "PM",hours_of_operation_wenesday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_thursday_open_hour = 1,hours_of_operation_thursday_open_minutes = 30,hours_of_operation_thursday_open_am_pm = "AM",hours_of_operation_thursday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_thursday_close_hour = 12,hours_of_operation_thursday_close_minutes = 0,hours_of_operation_thursday_close_am_pm = "PM",hours_of_operation_thursday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_friday_open_hour = 1,hours_of_operation_friday_open_minutes = 30,hours_of_operation_friday_open_am_pm = "AM",hours_of_operation_friday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_friday_close_hour = 12,hours_of_operation_friday_close_minutes = 0,hours_of_operation_friday_close_am_pm = "PM",hours_of_operation_friday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_saturday_open_hour = 1,hours_of_operation_saturday_open_minutes = 30,hours_of_operation_saturday_open_am_pm = "AM",hours_of_operation_saturday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_saturday_close_hour = 12,hours_of_operation_saturday_close_minutes = 0,hours_of_operation_saturday_close_am_pm = "PM",hours_of_operation_saturday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),
        hours_of_operation_sunday_open_hour = 1,hours_of_operation_sunday_open_minutes = 30,hours_of_operation_sunday_open_am_pm = "AM",hours_of_operation_sunday_open_time =  datetime.datetime.strptime("1:30",'%H:%M'),hours_of_operation_sunday_close_hour = 12,hours_of_operation_sunday_close_minutes = 0,hours_of_operation_sunday_close_am_pm = "PM",hours_of_operation_sunday_close_time = datetime.datetime.strptime("12:00",'%H:%M'),        
        )
    
    def test_animals_can_speak(self):
        demo = Restaurant.objects.get(restaurant_name="thetest")
        self.assertEqual(demo.hours_of_operation_monday_open_am_pm,"AM")
        self.assertEqual(demo.hours_of_operation_monday_open_hour,1)
        time = datetime.time(hour=1,minute=30)
        self.assertEqual(demo.hours_of_operation_sunday_open_time,time)