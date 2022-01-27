from django.shortcuts import render, HttpResponse
from datetime import datetime

# Create your views here.
from .models import Employee


def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html', context)


def add_emp(request):
    if request.method=='POST':
        #print('post')
        print(request.POST)
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        dept = request.POST['dept']
        role = request.POST['role']
        bonus = request.POST['bonus']
        emp=Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,role_id=role,bonus=bonus, hire_date=datetime.now())
        emp.save()
        return HttpResponse("Employee Added Successfully")
    else:
        print('get')
        return render(request,'add_emp.html')


def remove_emp(request):
    return render(request,'remove_emp.html')


def filter_emp(request):
    return render(request,'filter_emp.html')