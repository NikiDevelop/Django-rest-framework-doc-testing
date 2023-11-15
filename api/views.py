from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework import viewsets
from .models import User
# Create your views here.


# Importamos ViewSets que nos va a definir el comportamiento de la vista
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer