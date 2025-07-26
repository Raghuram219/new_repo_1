from django.shortcuts import render
from rest_framework import viewsets
from app.models import *
from app.serializers import *

from rest_framework.permissions import IsAuthenticated,AllowAny




class BooksView(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    action_serializers = {
        'create':StudentCreateSerializer,
        'list':StudentSerializer
    }

class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

