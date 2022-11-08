import csv
import re
import sys
sys.path.append("/api/restaurants")
from restaurants.apis.models import Restaurant
import datetime

def run():
    
    with open("restaurants.csv") as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            restaurant_info = {}
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
                P = Restaurant.objects.get_or_create(restaurant_name=restuarant)
                for day,time_details in times.items():
                    time_open = convert_time(time_details[0])
                    time_close = convert_time(time_details[1])
                    print("after convert")
                    print(time_open)
                    print("after convert")
                    print(time_close)
                    open_hour= time_open[0:2]
                    open_min = time_open[3:5]
                    open_am_pm = time_open[-2:]
                    close_hour= time_close[0:2]
                    close_min = time_close[3:5]
                    close_am_pm = time_close[-2:]
                        
                    #converts to get datetime object to put in database
                    if time_open[-2:] == "AM" and time_open[:2] == "12":
                        time_open = "00" + time_open[2:-2]
                        print(11)
                        print(time_open)
                    elif time_open[-2:] == "AM":
                        time_open = time_open[:-2]
                        print(12)
                        print(time_open)
                    elif time_open[-2:] == "PM" and time_open[:2] == "12":
                        time_open = time_open[:-2]
                        print(13)
                        print(time_open)
                    else:
                        time_open = str(int(time_open[:2]) + 12) + time_open[2:5]
                        print(14)
                        print(time_open)
                    #print(time_open[0:-2])
                    print("Heres 3")
                    print(time_open)
                    open_times = datetime.datetime.strptime(time_open,'%H:%M')



                    #print("Here z")
                    #print(time_close)
                    if time_close[-2:] == "AM" and time_close[:2] == "12":
                        time_close = "00" + time_close[2:-2]
                        print(1)
                        print(time_close)
                    elif time_close[-2:] == "AM":
                        time_close = time_close[:-2]
                        print(2)
                        print(time_close)
                    elif time_close[-2:] == "PM" and time_close[:2] == "12":
                        time_close = time_close[:-2]
                        print(3)
                        print(time_close)
                    else:
                        time_close = str(int(time_close[:2]) + 12) + time_close[2:5]
                        print(4)
                        print(time_close)
                        # time_close = str(time_close)
                    print("Heres 2")
                    print(time_close)
                    close_times =  datetime.datetime.strptime(time_close,'%H:%M')
                    # close_times = datetime.time.strftime(close_times,'%H:%M%p')

                    # #print(open_times)
                    # #print(close_times)
            
                    if day == "Mon":
                        # time_open = convert_time(time[0])
                        # time_close = convert_time(time[0])
                        # #print("moooooon")
                        # open_hour= time_open[0:2]
                        # #print(open_hour)
                        # #print("moooooon2")
                        # open_min = time_open[3:5]
                        # #print(open_min)
                        # #print("moooooon3")
                        # open_am_pm = time_open[5:7]
                        # #print(open_am_pm)
                        # close_hour= time_close[0:2]
                        # close_min = time_close[3:5]
                        # close_am_pm = time_close[5:7]
                        # if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                            
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_monday_open_hour=open_hour,
                                hours_of_operation_monday_open_minutes=open_min,
                                hours_of_operation_monday_open_am_pm=open_am_pm,
                                hours_of_operation_monday_close_hour = close_hour,
                                hours_of_operation_monday_close_minutes = close_min,
                                hours_of_operation_monday_close_am_pm = close_am_pm,
                                hours_of_operation_monday_open_time = open_times,
                                hours_of_operation_monday_close_time = close_times
                                )
                        )
                            
                            # ,hours_of_operation_monday_close=convert_time(time[1])))
                    if day == "Tues":
                    #     if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_tuesday_open=convert_time(time[0]),hours_of_operation_tuesday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_tuesday_open_hour=open_hour,
                                hours_of_operation_tuesday_open_minutes=open_min,
                                hours_of_operation_tuesday_open_am_pm=open_am_pm,
                                hours_of_operation_tuesday_close_hour = close_hour,
                                hours_of_operation_tuesday_close_minutes = close_min,
                                hours_of_operation_tuesday_close_am_pm = close_am_pm,
                                hours_of_operation_tuesday_open_time = open_times,
                                hours_of_operation_tuesday_close_time = close_times
                                )
                        )
                    if day == "Wed":
                    #     if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_wenesday_open=convert_time(time[0]),hours_of_operation_wenesday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_wenesday_open_hour=open_hour,
                                hours_of_operation_wenesday_open_minutes=open_min,
                                hours_of_operation_wenesday_open_am_pm=open_am_pm,
                                hours_of_operation_wenesday_close_hour = close_hour,
                                hours_of_operation_wenesday_close_minutes = close_min,
                                hours_of_operation_wenesday_close_am_pm = close_am_pm,
                                hours_of_operation_wenesday_open_time = open_times,
                                hours_of_operation_wenesday_close_time = close_times
                                )
                        )
                    if day == "Thu":
                    #     if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_thursday_open=convert_time(time[0]),hours_of_operation_thursday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_thursday_open_hour=open_hour,
                                hours_of_operation_thursday_open_minutes=open_min,
                                hours_of_operation_thursday_open_am_pm=open_am_pm,
                                hours_of_operation_thursday_close_hour = close_hour,
                                hours_of_operation_thursday_close_minutes = close_min,
                                hours_of_operation_thursday_close_am_pm = close_am_pm,
                                hours_of_operation_wenesday_open_time = open_times,
                                hours_of_operation_wenesday_close_time = close_times
                                )
                        )
                    if day == "Fri":
                        # if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_friday_open=convert_time(time[0]),hours_of_operation_friday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_friday_open_hour=open_hour,
                                hours_of_operation_friday_open_minutes=open_min,
                                hours_of_operation_friday_open_am_pm=open_am_pm,
                                hours_of_operation_friday_close_hour = close_hour,
                                hours_of_operation_friday_close_minutes = close_min,
                                hours_of_operation_friday_close_am_pm = close_am_pm,
                                hours_of_operation_friday_open_time = open_times,
                                hours_of_operation_friday_close_time = close_times
                                )
                        )
                    if day == "Sat":
                        # if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_saturday_open=convert_time(time[0]),hours_of_operation_saturday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_saturday_open_hour=open_hour,
                                hours_of_operation_saturday_open_minutes=open_min,
                                hours_of_operation_saturday_open_am_pm=open_am_pm,
                                hours_of_operation_saturday_close_hour = close_hour,
                                hours_of_operation_saturday_close_minutes = close_min,
                                hours_of_operation_saturday_close_am_pm = close_am_pm,
                                hours_of_operation_saturday_open_time = open_times,
                                hours_of_operation_saturday_close_time = close_times
                                )
                        )
                    if day == "Sun":  
                        # if "42nd" in restaurant_name:
                            #print(day)
                            #print(time[0])
                            #print(time[1])                  
                        # #print(Restaurant.objects.filter(restaurant_name=restaurant_name).update(hours_of_operation_sunday_open=convert_time(time[0]),hours_of_operation_sunday_close=convert_time(time[1])))
                        print(Restaurant.objects.filter(restaurant_name=restaurant_name)
                            .update(
                                hours_of_operation_sunday_open_hour=open_hour,
                                hours_of_operation_sunday_open_minutes=open_min,
                                hours_of_operation_sunday_open_am_pm=open_am_pm,
                                hours_of_operation_sunday_close_hour = close_hour,
                                hours_of_operation_sunday_close_minutes = close_min,
                                hours_of_operation_sunday_close_am_pm = close_am_pm,
                                hours_of_operation_sunday_open_time = open_times,
                                hours_of_operation_sunday_close_time = close_times
                                )
                        ) 



                   
def add_to_days_and_time(array, days_of_week,hours,restaurant_name):
    spec_times = {days_of_week:hours}
    
    if restaurant_name not in array:
        array[restaurant_name] = spec_times
    else:
        array[restaurant_name].update(spec_times)

def convert_time(hour,*name):
    # #print(f"in - {hour}")
    new_string = ""
    if ":30" in hour:
        new_string = hour
    if ":00" in hour:
        new_string = hour
    if ":30" not in hour and ":00" not in hour:
        new_string = hour.replace(" ",":00")     
    if ":30" not in hour and ":00" not in hour:
        new_string = hour.replace(" ",":00")
    if ":30" not in hour and ":00" not in hour:
        new_string = hour.replace(" ",":00")
    if 'a' in hour:
        new_string = new_string.replace('a','AM')
    if 'p' in hour:
        new_string = new_string.replace('p','PM')
    if "am" in new_string:
        new_string = new_string.replace('am','AM')
    if "pm" in new_string:
        new_string = new_string.replace('pm','PM')
    if " " in new_string:
        new_string = new_string.replace(' ','')
    if ":" in new_string[0:2]:
        new_string = "0" + new_string
    # if len(new_string) == 6 and " " not in new_string and "pm" not in new_string and "am" not in new_string:
    #print(new_string)
    return new_string
    # if " " in new_string and len(new_string) == 6:
    #     return str(0)+new_string.replace(" ","")
    # if " " in new_string and len(new_string) == 7:
    #     return str(0)+new_string.replace(" ","")
    # if " " in new_string and len(new_string) == 8:
    #     return new_string.replace(" ","")

    # return new_string
    # if len(new_string) == 6:
    #     return str(0)+new_string
    # if len(new_string) == 7 and " " in new_string:
    #     return (str(0)+new_string).replace(" ", "")
    # if len(new_string) == 8 and " " in new_string:
    #     return (new_string).replace(" ", "")  
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
        else:
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

