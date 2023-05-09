from django.shortcuts import render
from django.http import HttpResponse
from .models import Place

def home(request):
    all = Place.objects.all()
    return render(request,'home.html',{'all':all})
# Create your views here.
def detail(requset,place_id):
     all = Place.objects.get(id=place_id)
     return  render(requset,'detail.html',{'place':all})