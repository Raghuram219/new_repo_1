from rest_framework import serializers
from app.models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__' 

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__' 

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' 

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

class StudentSerializer(serializers.ModelSerializer):
    dept=DepartmentSerializer(many=False)
    books=BooksSerializer(many=True)
    class Meta:
        model = Student
        fields = ('id','name','dept','books')