import csv
import re
import sys
sys.path.append("/api/restaurants")
from restaurants.apis.models import Restaurant

def run():
    
    with open("restaurants.csv") as f:
        reader = csv.reader(f)
        next(reader)
        restaurant_info = {}
        for row in reader:
            if row[0]:
                restaurant_name=row[0]
                if "/" in row[1]:
                    times = row[1].split("/")
                    for time in times:
                        if "," in time:
                            days = re.findall("(^[a-zA-Z]*-[a-zA-Z]*),* ([a-zA-Z]*)",time)[0]
                            hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                            num_days = convert_to_week_array(days)
                            for day in num_days:
                                day_of_week = weekday_converter(day)
                                add_to_days_and_time(restaurant_info,day_of_week,hours,restaurant_name)
                            
                        else:
                            days = re.findall("[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]*-*[a-zA-Z]*",time)[0]
                            hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                            num_days = convert_to_week_array(days)
                            for day in num_days:
                                day_of_week = weekday_converter(day)
                                add_to_days_and_time(restaurant_info,day_of_week,hours,restaurant_name)
                            

                else:
                    time = row[1]
                    if "," in time:
                            days = re.findall("(^[a-zA-Z]*),* ([a-zA-Z]*-[a-zA-Z]*)",time)[0]
                            hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                            num_days = convert_to_week_array(days)
                            for day in num_days:
                                day_of_week = weekday_converter(day)
                                add_to_days_and_time(restaurant_info,day_of_week,hours,restaurant_name)
                    
                    else:
                        days = re.findall("^[a-zA-Z]*-*[a-zA-Z]*",time)[0]
                        hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                        num_days = convert_to_week_array(days)
                        for day in num_days:
                            day_of_week = weekday_converter(day)
                            add_to_days_and_time(restaurant_info,day_of_week,hours,restaurant_name)
                
                for restuarant,times in restaurant_info.items():
                    string = f"{restuarant} is open:"
                    for day,time in times.items():
                        P = Restaurant(restaurant_name=restuarant)
                        Restaurant.save

    #          """
    #         hours_of_operation_monday_open =  models.TimeField()
    # hours_of_operation_monday_close = models.TimeField()
    # hours_of_operation_tuesday_open = models.TimeField()
    # hours_of_operation_tuesday_close = models.TimeField()
    # hours_of_operation_wenesday_open = models.TimeField()
    # hours_of_operation_wenesday_close = models.TimeField()
    # hours_of_operation_thursday_open = models.TimeField()
    # hours_of_operation_thursday_close = models.TimeField()
    # hours_of_operation_friday_open = models.TimeField()
    # hours_of_operation_friday_close = models.TimeField()
    # hours_of_operation_saturday_open = models.TimeField()
    # hours_of_operation_saturday_close = models.TimeField()
    # hours_of_operation_sunday_open = models.TimeField()
    # hours_of_operation_sunday_close = models.TimeField()
    # # """
    #                 string = string + " " + str(day) +" opens->" + str(time[0]) + " and closes->" + str(time[1])
    #                 print(string)
         


                   
def add_to_days_and_time(array, days_of_week,hours,restaurant_name):
    spec_times = {days_of_week:hours}
    if restaurant_name not in array:
        array[restaurant_name] = spec_times
    else:
        array[restaurant_name].update(spec_times)

def convert_to_week_array(days):
    #days of week in number format 
    # days_of_week = ["Mon","Tues","Wens","Thurs","Fri","Sat","Sun"]
    days_of_week = [0,1,2,3,4,5,6,7]
    days_array = []
    if type(days) == tuple:
        for index in days:
            if "-" in index: 
                days_in_between = index.split("-")
                start_day = weekday_converter(days_in_between[0])
                end_day = weekday_converter(days_in_between[1])+1
                days_open = days_of_week[days_of_week[start_day]:days_of_week[end_day]]
                days_array = days_array + days_open
            else:
                day = weekday_converter(index)
                days_array.append(day)
    else:

        if "-" in days: 
            days_in_between = days.split("-")
            start_day = weekday_converter(days_in_between[0])
            end_day = weekday_converter(days_in_between[1])+1
            days_open = days_of_week[days_of_week[start_day]:days_of_week[end_day]]
            days_array = days_array + days_open
        if days and not "-":
            day = weekday_converter(days)
            days_array.append(day)

    return days_array


    

def weekday_converter(day):
    if day == "Mon":
        return 0

    elif day == 0:
        return "Mon"
    
    elif day == "Tues":
        return 1
    
    elif day == 1:
        return "Tues"  

    elif day == "Wed":
        return 2

    elif day == 2:
        return "Wed"
    
    elif day == "Thu":
        return 3

    elif day == 3:
        return "Thu"
    
    elif day == "Fri":
        return 4

    elif day == 4:
        return "Fri"
    
    elif day == "Sat":
        return 5

    elif day == 5:
        return "Sat"
    
    elif day == "Sun":
        return 6

    elif day == 6:
        return "Sun"

    elif day == "Other":
        return 7

    elif day == 7:
        return "Other"








    """
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
    """


            # _, created = Restaurant.objects.get_or_create(
            #     restaurant_name=row[0],
            #     last_name=row[1],
            #     middle_name=row[2],
            #     )