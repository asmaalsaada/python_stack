from django.shortcuts import redirect, render ,HttpResponse
from .models import Users

# Create your views here.
def index(request):
    context = {
        "Table_of_Users" : Users.objects.all() 
    }
    return render(request, "index.html",context) 
def show(request):
    Users.objects.create(
    first_name=request.POST['firstName'],
    last_name=request.POST['lastName'],
    email_address=request.POST['email_address'],
    age=request.POST['age'])
    return redirect('/')
def get(request,number):

    context = {
        "first_name_view" :  Users.objects.get(id = number)
    }

    return render(request,'get.html',context)