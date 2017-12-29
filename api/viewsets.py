# -*- coding: utf-8 -*-

from rest_framework import viewsets
from src.models import Employee
from api.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
