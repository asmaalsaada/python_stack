from django.shortcuts import render, HttpResponse,redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold'  not in request.session:
        request.session['gold'] = 0 #initilize the gold to 0 
    return render(request,"index.html")
def process(request):
    request.session['time'] = strftime("%Y-%m- %d %H:%M %p", gmtime())
    if 'farm_log' not in request.session:
        request.session['farm_log']=[]
    if 'cave_log' not in request.session:
        request.session['cave_log']=[]
    if 'house_log' not in request.session:
        request.session['house_log']=[]
    if 'casino_log' not in request.session:
        request.session['casino_log']=[]
    if request.POST['inp'] == 'farm':
        x=random.randint(10,20)
        request.session['farm'] = x # generate a random number
        farm_log="you earned "+str(x)+" gold from farm " + request.session['time']
        request.session['farm_log'].append(farm_log)
        request.session['gold'] += request.session['farm']
    if request.POST['inp'] == 'cave':
        j=random.randint(5,10)
        request.session['cave'] = j # generate a random number
        cave_log="you earned "+str(j)+" gold from cave " + request.session['time']
        request.session['cave_log'].append(cave_log)
        request.session['gold'] += request.session['cave']
    if request.POST['inp'] == 'house':
        f=random.randint(2,5)
        request.session['house'] = f # generate a random number
        house_log="you earned "+str(f)+" gold from house " + request.session['time']
        request.session['house_log'].append(house_log)
        request.session['gold'] += request.session['house']
    if request.POST['inp'] == 'casino':
        d=random.randint(-50,50)
        request.session['casino'] = d # generate a random number
        casino_log="you got "+str(d)+" gold from casino " + request.session['time']
        request.session['casino_log'].append(casino_log)
        request.session['gold'] += request.session['casino']
    return redirect('/')

