import datetime
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from restaurants.apis.serializers import UserSerializer, GroupSerializer,RestaurantInfoSerializer,RestaurantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Restaurant
from rest_framework import status
from django.db import connection
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
import json as simplejson

class RestaurantsApiView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = RestaurantSerializer
    http_method_names = ['get', ]
    queryset = Restaurant.objects.none()

    def get_queryset(self):
        return(Restaurant.objects.all())
        
    # def list(self, request):
    #     query_set = Restaurant.objects.all()
    #     datetimestamp=self.request.query_params.get('datetime')
    #     print(datetimestamp)
    #     return Response(self.serializer_class(query_set, many=True).data,
    #                     status=status.HTTP_200_OK)

class RestaurantsApiViewDetails(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = RestaurantInfoSerializer
    http_method_names = ['get', ]
    queryset = Restaurant.objects.none()
    
    def get_queryset(self):
        if self.request.query_params:
            datetimestamp=self.request.query_params.get('datetime')
            print(datetimestamp)
            datetime_param = datetimestamp.split('T')
            day = datetime.datetime.strptime(datetime_param[0],'%Y-%m-%d').strftime('%A')
            #examplecode - http://localhost:8000/restaurantsinfo/?datetime=2021-04-19T09:14pm
            time_strip = datetime_param[1]
            time = datetime.datetime.strptime(time_strip,"%H:%M%p").time()
            hour = str(time.hour)
            if len(hour) == 1:
                # hour = str(0)+hour
                hour = int(hour)              
            min = str(time.minute)
            min_int = int(min)
            if min_int >= 30:
                min_int = 30
            else:
                min_int = 00
            print("this is time strip")
            print(time_strip)
            if "am" in time_strip:
                time_strip = time_strip.replace("am","AM")
            if "pm" in time_strip:
                time_strip = time_strip.replace("pm","PM")
            print(time_strip)
            if time_strip[-2:] == "AM" and time_strip[:2] == "12":
                        time_strip = "00" + time_strip[2:-2]
                        print(11)
                        print(time_strip)
            elif time_strip[-2:] == "AM":
                time_strip = time_strip[:-2]
                print(12)
                print(time_strip)
            elif time_strip[-2:] == "PM" and time_strip[:2] == "12":
                time_strip = time_strip[:-2]
                print(13)
                print(time_strip)
            else:
                time_strip = str(int(time_strip[:2]) + 12) + time_strip[2:5]
                print(14)
                print(time_strip)
            #print(time_open[0:-2])
            print("Heres 3")
            print(time_strip)
            time_strip = datetime.datetime.strptime(time_strip,'%H:%M')

            
            # am_or_pm = time_strip[-2:]
            # time_search = f'{hour}:{min_int}'
            # print(time)
            # print(time_search)
            # Dataset.objects.filter(i_end_int__gte=x,i_begin_int__lte=x)

            if day == "Monday":
                # r = Restaurant.objects.filter(hours_of_operation_monday_open_hour__lte=hour,hours_of_operation_monday_open_minutes__lte = min, hours_of_operation_monday_open_am_pm__lte = am_or_pm,
                #                              hours_of_operation_monday_close_hour__gte=hour,hours_of_operation_monday_close_minutes__gte = min, hours_of_operation_monday_close_am_pm__gte = am_or_pm
                #                             )
                r = Restaurant.objects.filter(hours_of_operation_monday_open_time__lte=time_strip,hours_of_operation_monday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data



            if day == "Tuesday":
                r = Restaurant.objects.filter(hours_of_operation_monday_open__gte=time_search,hours_of_operation_monday_open__lte=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Wenesday":
                r = Restaurant.objects.filter(hours_of_operation_monday_open__gte=time_search,hours_of_operation_monday_open__lte=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Thursay":
                r = Restaurant.objects.filter(hours_of_operation_monday_open__gte=time_search,hours_of_operation_monday_open__lte=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Friday":
                r = Restaurant.objects.filter(hours_of_operation_monday_open__gte=time_search,hours_of_operation_monday_open__lte=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Saturday":
                r = Restaurant.objects.filter(hours_of_operation_saturday_open=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Sunday":
                r = Restaurant.objects.filter(hours_of_operation_sunday_open=time_search)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
    

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



# #get filter to spit out days
# class RestaurantsQueryApiView(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
    # queryset = Restaurant.objects.all()
    # serializer_class = RestaurantInfoSerializer
    # queryset = Restaurant.objects.all()
    # # serializer = RestaurantInfoSerializer(queryset,many=all)
    # #add to have built-in django authentication
    # # permission_classes = [permissions.IsAuthenticated]
    # http_method_names = ['get']
    # def get_queryset(self):
    #     datetimestamp=self.request.query_params.get('datetime')
    #     print(datetimestamp)
    #     queryset = Restaurant.objects.all()
    #     serializer_class = RestaurantInfoSerializer
    #     # if self.request.query_params:
    #     #     # datetime==self.request.query_params.get('datetime'):
    #     #     datetimestamp=self.request.query_params.get('datetime')
    #     #     print(datetimestamp)
    #     #     datetime_param = datetimestamp.split('T')
    #     #     # time = 
    #     #     day = datetime.datetime.strptime(datetime_param[0],'%Y-%m-%d').strftime('%A')
    #     #     #examplecode - http://localhost:8000/restaurants/view/?datetime=2021-04-19T09:14pm
    #     #     time_strip = datetime_param[1]
    #     #     time = datetime.datetime.strptime(time_strip,"%I:%M%p").time()
    #     #     print("here")
    #     #     print(time.hour)
    #     #     print(time.minute)
    #     #     print(day)
    #     #     # queryset = Restaurant.objects.all()
    #     #     # serializer = RestaurantInfoSerializer(queryset,many=all)
    #     #     # if day == "Monday":
    #     #     #     queryset = Restaurant.objects.values_list('restaurant_name','hours_of_operation_monday_open')
    #     #     #     queryset = queryset.all()
    #     #     #     # print(queryset)
    #     #     #     return queryset
    #     #     #     # cursor = connection.cursor()
    #     #     #     # cursor.execute('''SELECT restaurants_restaurant.restaurant_name,restaurants_restaurant.hours_of_operation_monday_open,restaurants_restaurant.hours_of_operation_monday_close''')
    #     #         # row = cursor.fetchall()
    #             # print(row)
    #             # return row


    #         # cursor = connection.cursor()
    #         # cursor.execute('''SELECT count(*) FROM people_person''')
    #         # row = cursor.fetchall()
    #         # return row

    #         # """
    #         # Though this looks like three database hits, in fact it hits the database only once, at the last line (print(q)). In general, the results of a QuerySet aren’t fetched from the database until you “ask” for them. When you do, the QuerySet is evaluated by accessing the database. For more details on exactly when evaluation takes place, see When QuerySets are evaluated.
    #         # """
        
    #     # else:
    #     # queryset = Restaurant.objects.all()
    #     queryset = Restaurant.objects.all()
    #     serializer = RestaurantInfoSerializer(queryset,many=all)
        # print(queryset)
        # return queryset
    #     queryset = Restaurant.objects.all()
    #     # datetime=self.request.query_params.get('datetime')
    #     return queryset

    # def get_queryset(self):
    #     queryset = Restaurant.objects.all()
    #     datetime=self.request.query_params.get('datetime')
    #     #format needs to be 1970-01-01 00:00:01
    #     day = datetime.datetime.strptime('datetime', '%B-%d-%Y').strftime('%A')
        
        # cursor = connection.cursor()
        # cursor.execute('''SELECT count(*) FROM people_person''')
        # row = cursor.fetchall()
        # return row


