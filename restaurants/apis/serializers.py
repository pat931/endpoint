from .models import Restaurant
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class RestaurantInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        time_format = ['%I:%M %p',]
        # fields = ['0', 'name', 'category']
        restaurant_name = serializers.CharField(max_length=100)
        hours_of_operation_monday_open =  serializers.TimeField(input_formats=time_format)
        hours_of_operation_monday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_tuesday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_tuesday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_wenesday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_wenesday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_thursday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_thursday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_friday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_friday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_saturday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_saturday_close = serializers.TimeField(input_formats=time_format)
        hours_of_operation_sunday_open = serializers.TimeField(input_formats=time_format)
        hours_of_operation_sunday_close = serializers.TimeField(input_formats=time_format)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
"""
Very similarly to the model serializer, we also have the option to use a HyperlinkedModelSerializer. The main difference between the two is the ModelSerializer will have an id field as the primary key, the HyperlinkedModelSerializer will use a url field instead of an id. Depending on what you need, you will want to choose one or the other. But it is set up the same way, here is an example:
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'id', 'account_name', 'users', 'created'
        """