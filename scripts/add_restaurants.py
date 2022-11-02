import csv
import re
import sys
sys.path.insert(0, "API/restaurants/apis/models.py")
import Restaurant
def run():
    with open("restaurants.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]:
                restaurant_name=row[0]
                if "/" in row[1]:
                    times = row[1].split("/")
                    for time in times:
                        # if any(day.lower() in time.lower() for day in days_of_week.keys()):
                        if "," in time:
                            days = re.findall("(^[a-zA-Z]*-[a-zA-Z]*),* ([a-zA-Z]*)",time)
                            hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                        else:
                            days = re.findall("[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]*-*[a-zA-Z]*",time)
                            hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)

                        print(restaurant_name + ":" + str(days[0]) + str(hours))
                        
                else:
                    time = row[1]
                    days = re.findall("^[a-zA-Z]*-*[a-zA-Z]*",time)
                    hours = re.findall("[0-9]*:*[0-9]* [am|pm]",time)
                    print(restaurant_name + ":" + str(days[0]) + str(hours))

def time_of_week(weekday,opening,closing):
    days_of_week = {"Mon":,"Tues","Wens","Thurs","Fri","Sat","Sun"]
        if "-" not in weekday:
            day = Restaurant()




                # for time in times:
                #     if "Mon-Sun" in time
                # print(times)       







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