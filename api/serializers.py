from rest_framework import serializers
from src.models import Employee


class EmployeeSerialize(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
