from django.urls import path
from . import views

urlpatterns=[
path('',views.hello,name='hello'),
path('gm/',views.gm,name='gm'),
path('ge/',views.ge,name='ge'),
path('gn/',views.gn,name='gn'),
path('temp/',views.template_view,name='template'),
path('info/',views.my_info),
path('wish/',views.wish),
 ]