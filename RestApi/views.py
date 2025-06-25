from django.shortcuts import render
from rest_framework import generics 
from .serializor import employeeSerializer
from .models import employee  
# Create your views here.


class employeeList(generics.ListCreateAPIView):
	queryset = employee.objects.all()
	serializer_class = employeeSerializer