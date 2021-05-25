from dojo_ninjas_app.models import Dojos
from django.shortcuts import render,redirect
from .models import Dojos,Ninja

def index(request):
    context = {
        'dojos' : Dojos.objects.all(),
        'ninja' : Ninja.objects.all(),
    }
    return render(request,"index.html",context)

def add_dojo(request):
    name_from = request.POST['dojo_name']
    city_from = request.POST['dojo_city']
    state_from = request.POST['dojo_state']
    Dojos.objects.create(name=name_from,city=city_from,state=state_from)
    return redirect('/')
def dojos_list(request):
    context = {
        'dojos' : Dojos.objects.all(),
    }
    return redirect('/',context)
def add_ninja(request):
    first_from = request.POST['first_name']
    last_from = request.POST['last_name']
    # id_from =  request.POST['dojo']
    
    Ninja.objects.create(first_name=first_from,last_name=last_from,dojo=Dojos.objects.get(name=request.POST['dojo_menu']))
    return redirect('/')
