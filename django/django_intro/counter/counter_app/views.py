from django.shortcuts import render, HttpResponse,redirect

def counter(request):
    if 'counter' not in request.session:
        request.session['counter'] =1
    else:
        request.session['counter'] +=1
    return render(request, 'index.html')
def destroy(request):
    del request.session['counter']
    return redirect('/')
def plus_two(request):
    request.session['counter'] +=1
    return redirect('/') 
