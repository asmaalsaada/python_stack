from django.shortcuts import render,redirect
# Create your views here.
def index(request):
    return render(request,"index.html")
def create_user(request):
    request.session['name'] = request.POST['name']
    request.session['dojo_loc'] = request.POST['dojo_loc']
    request.session['fav_lan'] = request.POST['fav_lan']
    request.session ['comment'] = request.POST['text_box']
    
    return redirect("/results")
def results(request):
    # context = {
    # 'name': request.session['name'],
    # "dojo_" : request.session['dojo_loc'],
    # "fv_lan": request.session['fav_lan'],
    # "comment": request.session ['comment'],
    # }
    return render(request,"show.html")
