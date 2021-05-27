from typing import ContextManager
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

from .models import Users
import bcrypt

def index(request):
    if 'userid'  in request.session:
        return redirect('/success')
    context = {
        'users' : Users.objects.all()
    }
    return render(request,"index.html",context)
def login(request):
    if 'userid' in request.session:
        return redirect('/success')
    errors = Users.objects.login_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        users = Users.objects.filter(email=request.POST['email'])
        if users:
            if len(users) == 0 :
                return redirect('/')
            user = users.first()
            if bcrypt.checkpw(request.POST['passwd'].encode(), user.password.encode()):
                request.session['userid'] = user.id
                return redirect('/success')
        return redirect('/')
def register(request): 
    if 'userid'  in request.session:
        return redirect('/success')
    password = request.POST['passwd']
    hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
    errors = Users.objects.reg_validator(request.POST)
    if len(errors) > 0 : 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else : 
        user = Users.objects.create(first_name=request.POST['f_name'],last_name=request.POST['l_name'],email=request.POST['email'],password=hash1)
        messages.success(request, "User successfully created")
        return render(request,"success.html")
def success(request):
    if 'userid'  in request.session:
        context = {
            'user' : Users.objects.get(id= request.session["userid"])
        }
        return render(request,"success.html",context)
    return redirect('/')
def logout(request):
    if 'userid' in request.session:
        request.session.clear()
    return redirect('/')