import datetime
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from restaurants.apis.serializers import UserSerializer, GroupSerializer,RestaurantInfoSerializer,RestaurantSerializer
from .models import Restaurant
from django.db import connection

class RestaurantsApiView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = RestaurantSerializer
    http_method_names = ['get', ]
    queryset = Restaurant.objects.none()

    def get_queryset(self):
        return(Restaurant.objects.all())
        
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
            time_strip = datetime_param[1]
            time = datetime.datetime.strptime(time_strip,"%H:%M%p").time()
            hour = str(time.hour)
            if len(hour) == 1:
                hour = int(hour)              
            min = str(time.minute)
            min_int = int(min)
            if min_int >= 30:
                min_int = 30
            else:
                min_int = 00
          
            if "am" in time_strip:
                time_strip = time_strip.replace("am","AM")
            if "pm" in time_strip:
                time_strip = time_strip.replace("pm","PM")

            if time_strip[-2:] == "AM" and time_strip[:2] == "12":
                        time_strip = "00" + time_strip[2:-2]
                       
            elif time_strip[-2:] == "AM":
                time_strip = time_strip[:-2]
              
            elif time_strip[-2:] == "PM" and time_strip[:2] == "12":
                time_strip = time_strip[:-2]
                
            else:
                time_strip = str(int(time_strip[:2]) + 12) + time_strip[2:5]
               
            time_strip = datetime.datetime.strptime(time_strip,'%H:%M')

            
        
            if day == "Monday":
                r = Restaurant.objects.filter(hours_of_operation_monday_open_time__lte=time_strip,hours_of_operation_monday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data

            if day == "Tuesday":
                r = Restaurant.objects.filter(hours_of_operation_tuesday_open_time__lte=time_strip,hours_of_operation_tuesday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Wenesday":
                r = Restaurant.objects.filter(hours_of_operation_wenesday_open_time__lte=time_strip,hours_of_operation_wenesday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Thursay":
                r = Restaurant.objects.filter(hours_of_operation_thursay_open_time__lte=time_strip,hours_of_operation_thursay_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Friday":
                r = Restaurant.objects.filter(hours_of_operation_friday_open_time__lte=time_strip,hours_of_operation_friday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Saturday":
                r = Restaurant.objects.filter(hours_of_operation_saturday_open_time__lte=time_strip,hours_of_operation_saturday_close_time__gte=time_strip)
                serializer = RestaurantInfoSerializer(r,many=True)
                return serializer.data
            if day == "Sunday":
                r = Restaurant.objects.filter(hours_of_operation_sunday_open_time__lte=time_strip,hours_of_operation_sunday_close_time__gte=time_strip)
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

def page_not_found_view(request, exception):
        return render(request, '404.html', status=404)