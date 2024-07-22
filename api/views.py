from django.shortcuts import render
from rest_framework.views import APIView;
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from teacher.models import Teacher
from classperiod.models import ClassPeriod
from classroom.models import Classroom
from course.models import Course
from .serializers import ClassPeriodSerializer, ClassroomSerializer, CourseSerializer, StudentSerializer, TeacherSerializer


class StudentListView(APIView):
    def get(self, response):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data,request.data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
    def put(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    
class ClassPeriodListView(APIView):
    def get(self, request):
        classperiod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classperiod, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ClassPeriodDetailView(APIView):
    def get(self, request, id):
        clasperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod)
        return Response(serializer.data)
    
    def put(self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(classperiod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete (self, request, id):
        classperiod = ClassPeriod.objects.get(id=id)
        classperiod.delete()
        return Response (status=status.HTTP_202_ACCEPTED)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TeacherDetailView(APIView):
    def get(self, request, id):
        teachers = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teachers)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response (status=status.HTTP_202_ACCEPTED)


class ClassroomListView(APIView):
    def get(self, request):
        classroom =  Classroom.objects.all()
        serializer = TeacherSerializer(classroom, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =  ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class  ClassroomDetailView(APIView):
    def get(self, request, id):
        Classroom =  Classroom.objects.get(id=id)
        serializer =  ClassroomSerializer(Classroom)
        return Response(serializer.data)
    def put(self, request, id):
        Classroom =  Classroom.objects.get(id=id)
        serializer = ClassroomSerializer(classroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        classroom =  Classroom.objects.get(id=id)
        classroom.delete()
        return Response (status=status.HTTP_202_ACCEPTED)
    
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Course.objects.get(id=id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete (self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response (status=status.HTTP_202_ACCEPTED)

    

