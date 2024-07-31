from django.contrib.sites import requests
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restapp2 import serializer
from restapp2.models import Students
from restapp2.serializer import StudentsSerializer
import requests

# Create your views here.


@api_view(['GET'])
def getData(request):
    app=Students.objects.all()
    serializer=StudentsSerializer(app,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer=StudentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteData(request,pk):
    app = Students.objects.get(Student_Id=pk)
    app.delete()
    return Response('Item successfully deleted')

class StudentListAPIView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

def student_list_view(request):
    response = requests.get('http://localhost:8000/api/students/')
    students = response.json()
    return render(request, 'index.html', {'students': students})

def student_update_view(request,stdid):
    std=get_object_or_404(Students,pk=stdid)
    if request.method=='POST':
        std.Student_Id=request.POST['stdid']
        std.First_Name = request.POST['fname']
        std.Last_Name = request.POST['lname']
        std.Age = request.POST['age']
        std.Address = request.POST['address']
        std.Course = request.POST['course']
        std.Location=request.POST['location']
        std.Phone=request.POST['phone']
        std.save()
        return redirect('/')
    return render(request,'update.html',{'student':std})

def student_delete_view(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return redirect('/')

def student_add(request):
    if request.method == 'POST':
        Student_Id = request.POST['stdid']
        First_Name = request.POST['fname']
        Last_Name = request.POST['lname']
        Age = request.POST['age']
        Address = request.POST['address']
        Course = request.POST['course']
        Location = request.POST['location']
        Phone = request.POST['phone']


        std = Students(
            Student_Id=Student_Id,
            First_Name=First_Name,
            Last_Name=Last_Name,
            Age=Age,
            Address=Address,
            Course=Course,
            Location=Location,
            Phone=Phone

        )
        std.save()
        return redirect('/')

    return render(request,'add.html')