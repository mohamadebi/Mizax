from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Place
from django.contrib import messages

def home(request):
    all = Place.objects.all()
    return render(request,'home.html',{'all':all})
# Create your views here.
def detail(requset,place_id):
     all = Place.objects.get(id=place_id)
     return  render(requset,'detail.html',{'place':all})


def delete(requset, place_id):
    Place.objects.get(id=place_id).delete()
    messages.success(requset,'Record deleted successfully',extra_tags="success")
    return redirect('home')