from django.shortcuts import render
from django.http import HttpResponse
from .models import Place

def home(request):
    all = Place.objects.all()
    return render(request,'home.html',{'all':all})
def say_hello(request):
    return render(request,'hello.html')
# Create your views here.
