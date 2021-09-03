from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg="hello guest Good Morning"
    elif h<16:
        msg = "hello guest Good Afternoon"
    elif h<21:
        msg = "hello guest Good Evening"
    else:
        msg = "hello guest Good Night"
    my_dict={'date':date,'msg':msg}
    return render(request,'myapp/results.html',my_dict)
