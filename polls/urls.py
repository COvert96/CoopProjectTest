from django.urls import path
from . import views



urlpatterns = [path('', views.polls),
               path('about', views.about)]