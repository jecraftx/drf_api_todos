from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create Read Update Delete 

class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class CreateTodo(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class =TodoSerializer

class DeleteTodo(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
