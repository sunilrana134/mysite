from django.shortcuts import render
from .models import Employee
# Create your views here.
def employee_info(request):
    employees=Employee.objects.all()
    return render(request,'myapp/results.html',{'employees':employees})
