from django.shortcuts import render
from django.http import HttpResponse
import datetime
def hello(request):
    return HttpResponse("hello world.")
# Create your views here.
def gm(request):
    return  HttpResponse("hello friends good morning")
def ge(request):
    return  HttpResponse("hello friends good evening")
def gn(request):
    return  HttpResponse("hello friends good night")
def template_view(request):
    dt=datetime.datetime.now()
    my_dict={'date':dt}
    return render (request,'polls/results.html',my_dict)

def my_info(request):
    name='sunil'
    rollno=4
    mark=92
    my_dict1={'name':name,'rollno':rollno,'mark':mark}
    return render(request,'polls/info.html',my_dict1)


def wish(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg='Hello Guest, Very Good'
    if h<12:
        msg=msg+'Morning..'
    elif h<16:
        msg=msg+'Afternoon..'
    elif h<21:
        msg=msg+'Evening..'
    else:
        msg=msg+'Night..'
    return render(request,'polls/greets.html',{'msg':msg,'date':date})



