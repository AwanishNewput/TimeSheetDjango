from rest_framework import serializers
from tracker.models import EmployeeDetail, TimeSchedual, TimeSheets
from django.contrib.auth.models import User
from tracker import models


class EmplSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetail
        fields = ('dob','address','contact','gender','role',
                  'created','updated')


class UserSerializer(serializers.ModelSerializer):

    UserInfo = serializers.HyperlinkedRelatedField(many=True, view_name='emp-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','last_login','username','UserInfo')


class TimeSchedualSerializer(serializers.HyperlinkedModelSerializer):
    usersId = serializers.ReadOnlyField(source='user_id.id')

    class Meta:
        model = TimeSchedual
        fields = ('usersId','work_date','chunk_id','M_time_in', 'M_time_out', 'L_time_in', 'L_time_out',
                  'N_time_in', 'N_time_out', 'work_desc')

    def validate(self, attrs):
        if attrs['L_time_in'] < attrs['M_time_in']:
            raise serializers.ValidationError("Lunch time should be greater then Morning time")

        elif attrs['L_time_in'] > attrs['L_time_out']:
            raise serializers.ValidationError("Lunch time can not be negative")

        elif attrs['M_time_out'] < attrs['M_time_in']:
            raise serializers.ValidationError("Working hours can not be negative")

        elif attrs['M_time_out'] < attrs['L_time_out']:
            raise serializers.ValidationError("You can not showing lunch time after leaving")

        return attrs


class TimeSheetSerializer(serializers.HyperlinkedModelSerializer):

    userValue = serializers.ReadOnlyField(source='user_id.id')

    class Meta:
        model = TimeSheets
        fields = ('userValue','work_date','chunk_id','in_time','out_time')
