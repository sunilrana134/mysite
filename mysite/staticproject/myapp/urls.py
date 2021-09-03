from django.urls import path
from . import views

urlpatterns=[
    path('msg/',views.date_time_view)
]