from datetime import datetime
from django.shortcuts import render , HttpResponse
from .models import Employee ,Department ,Role
# from django.db.models import QuerySet 
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request ,'index.html')

def view_emp(request):
    emps = Employee.objects.all()
    context = { "emps" : emps}
    print(context)
    return render(request ,'view_emp.html' , context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        new_employee = Employee(first_name = first_name , last_name = last_name , dept_id = dept , salary = salary , bonus = bonus , role_id = role ,phone = phone , hire_date =datetime.now())
        new_employee.save()
        return HttpResponse ("Employee added successfully !!!")
    
    elif request.method == "GET":
        return render(request ,'add_emp.html')
    
    else:
        return HttpResponse ("An Exception occured ! Employee is not saved.")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully !!")
        except:
            return HttpResponse("Please Choose a Valid Employee ")
    remps = Employee.objects.all()
    context1 = {
        "remps" : remps
    }
    return render(request ,'remove_emp.html' , context1)

def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]
        emps = Employee.objects.all()
        if name:
            emps = Employee.objects.filter(Q(first_name__icontains = name) | (Q(last_name__icontains = name)) )
        if dept:
            emps = emps.filter(Q(dept__name__icontains = dept))
        if role:
            emps = emps.filter(Q(role__name__icontains = role))
        context = {"emps": emps}
        return render(request ,'view_emp.html' , context)
    
    elif request.method == "GET":
        return render(request , 'filter_emp.html')
    
    else:
        return render(request ,'filter_emp.html')