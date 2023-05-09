from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hello/',views.say_hello),
    path('detail/<int:place_id>/',views.detail),


]