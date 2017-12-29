# -*- coding: utf-8 -*-

from rest_framework import serializers
from src.models import Employee


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')
