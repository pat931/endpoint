import csv
import sys
sys.path.insert(0, "API/restaurants/apis/models.py")
# fromimport Restaurant
def run():
    days_of_week = ["Mon","Tue","Wens","Thurs","Fri","Sat","Sun"]
    with open("restaurants.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]:
                restaurant_name=row[0]
            # if row[2]:
            #     times = row[1].split("/")
            #     for time in times:
            #         if "Mon-Sun" in time
                print(restaurant_name)       







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