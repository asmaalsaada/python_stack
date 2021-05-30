from typing import ContextManager
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages

from .models import Messages, Users, Comments
import bcrypt

def index(request):
    if 'userid'  in request.session:
        return redirect('/wall')
    context = {
        'users' : Users.objects.all()
    }
    return render(request,"index.html",context)
def login(request):
    if 'userid' in request.session:
        return redirect('/wall')
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
                return redirect('/wall')
        return redirect('/')
def register(request): 
    if 'userid'  in request.session:
        return redirect('/wall')
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
    msgs=Messages.objects.all()
    if 'userid'  in request.session:
        context = {
            'user' : Users.objects.get(id= request.session["userid"]),
            'msgs':msgs,
        }
        return render(request,"success.html",context)
    return redirect('/')
def logout(request):
    if 'userid' in request.session:
        request.session.clear()
    return redirect('/')
def posts(request):
    user_id = Users.objects.get(id= request.session["userid"])
    if 'userid'  in request.session:
        Messages.objects.create(message=request.POST['add_msg'],user_id=user_id)
    return redirect('/wall') 
def comments(request,id):
    user_id = Users.objects.get(id= request.session["userid"])
    message_id = Messages.objects.get(id=id)
    if 'userid'  in request.session:
        Comments.objects.create(comment=request.POST['comment'], user_id=user_id,message_id=message_id)
    return redirect('/wall') 
def del_msg(request,id):
    user_id = Users.objects.get(id= request.session["userid"])
    # message_id = Messages.objects.get(id=id)
    if 'userid'  in request.session:
        c=Messages.objects.get(user_id=user_id)
        c.delete()
    return redirect('/wall') 
    