from .models import Restaurant
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        restaurant_name = serializers.CharField(max_length=100)
        hours_of_operation_monday_open_hour =  serializers.IntegerField()
        hours_of_operation_monday_open_minutes = serializers.IntegerField()
        hours_of_operation_monday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_monday_open_time =  serializers.TimeField()
        hours_of_operation_monday_close_hour =  serializers.IntegerField()
        hours_of_operation_monday_close_minutes = serializers.IntegerField()
        hours_of_operation_monday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_monday_close_time =  serializers.TimeField()
        hours_of_operation_tuesday_open_hour =  serializers.IntegerField()
        hours_of_operation_tuesday_open_minutes = serializers.IntegerField()
        hours_of_operation_tuesday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_tuesday_open_time =  serializers.TimeField()
        hours_of_operation_tuesday_close_hour =  serializers.IntegerField()
        hours_of_operation_tuesday_close_minutes = serializers.IntegerField()
        hours_of_operation_tuesday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_tuesday_close_time =  serializers.TimeField()
        hours_of_operation_wenesday_open_hour =  serializers.IntegerField()
        hours_of_operation_wenesday_open_minutes = serializers.IntegerField()
        hours_of_operation_wenesday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_wenesday_open_time =  serializers.TimeField()
        hours_of_operation_wenesday_close_hour =  serializers.IntegerField()
        hours_of_operation_wenesday_close_minutes = serializers.IntegerField()
        hours_of_operation_wenesday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_wenesday_close_time =  serializers.TimeField()
        hours_of_operation_thursday_open_hour =  serializers.IntegerField()
        hours_of_operation_thursday_open_minutes = serializers.IntegerField()
        hours_of_operation_thursday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_thursday_open_time =  serializers.TimeField()
        hours_of_operation_thursday_close_hour =  serializers.IntegerField()
        hours_of_operation_thursday_close_minutes = serializers.IntegerField()
        hours_of_operation_thursday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_thursday_close_time =  serializers.TimeField()
        hours_of_operation_friday_open_hour =  serializers.IntegerField()
        hours_of_operation_friday_open_minutes = serializers.IntegerField()
        hours_of_operation_friday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_friday_open_time =  serializers.TimeField()
        hours_of_operation_friday_close_hour =  serializers.IntegerField()
        hours_of_operation_friday_close_minutes = serializers.IntegerField()
        hours_of_operation_friday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_friday_close_time =  serializers.TimeField()
        hours_of_operation_saturday_open_hour =  serializers.IntegerField()
        hours_of_operation_saturday_open_minutes = serializers.IntegerField()
        hours_of_operation_saturday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_saturday_open_time =  serializers.TimeField()
        hours_of_operation_saturday_close_hour =  serializers.IntegerField()
        hours_of_operation_saturday_close_minutes = serializers.IntegerField()
        hours_of_operation_saturday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_saturday_close_time =  serializers.TimeField()
        hours_of_operation_sunday_open_hour =  serializers.IntegerField()
        hours_of_operation_sunday_open_minutes = serializers.IntegerField()
        hours_of_operation_sunday_open_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_sunday_open_time =  serializers.TimeField()
        hours_of_operation_sunday_close_hour =  serializers.IntegerField()
        hours_of_operation_sunday_close_minutes = serializers.IntegerField()
        hours_of_operation_sunday_close_am_pm =  serializers.CharField(max_length=100)
        hours_of_operation_sunday_close_time =  serializers.TimeField()
        fields = '__all__'

class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        restaurant_set = RestaurantSerializer()
        fields = ['restaurant_name']  

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
