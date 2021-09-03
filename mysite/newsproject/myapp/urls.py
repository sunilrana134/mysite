
from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home_page),
path('movies/',views.movie_news),
    path('sports/',views.sports_news),
    path('politics/',views.politics_news)

]