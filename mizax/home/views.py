from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Place
from django.contrib import messages
from .forms import PlaceForm,PlaceUpdateForm



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

def update(requset, place_id):
    info = Place.objects.get(id=place_id)
    if requset.method == 'POST':
        form = PlaceUpdateForm(requset.POST,instance=info)
        if form.is_valid():
            form.save()
            messages.success(requset,'your info updated successfully','success')
            return redirect('detail',place_id)
    else:
        form = PlaceUpdateForm(instance=info)
    # messages.success(requset,'Record update successfully',extra_tags="success")

    return render(requset,'update.html',{'form':form})

def create (request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Place.objects.create(name = cd['name'],city=cd['city'],ticket_price=cd['ticket_price'],opentime=cd['opentime'])
            messages.success(request,'Place created successfully','success')
            return redirect('home')
    else:
        form = PlaceForm()
    return render(request, 'create.html' , {'form':form})
