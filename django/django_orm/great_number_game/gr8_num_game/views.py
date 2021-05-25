from django.shortcuts import redirect, render, HttpResponse
import random

def index(request):
    if "key" not in request.session:
        request.session['key'] =random.randint(1, 100)
    return render (request, "index.html")

def process(request): 
    guess_num=request.POST['input_number']
    if int(guess_num) > request.session['key']:
        request.session["res"]="high"
    elif int(guess_num) == request.session['key']:
        request.session["res"]="correct"
    else:
        request.session["res"]="low"
    return redirect ("/")



# def correct(request):
#     if request.POST['input_number'] == request.session['random_num']:
#         return render(request, "correct.html")
# def too_low(request):
#     if request.POST['input_number'] > request.session['random_num']:
#         return render(request,"too_high.html")
# def too_high(request):
#     if request.POST['input_number'] < request.session['random_num']:
#         return render(request,"too_low.html")
