from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class CreateReadEmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
