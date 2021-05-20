from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'html.index')
def random(request):
    import random
    random_num = request.session['random_num'] = random.randint(1, 100)
def correct(request):
    if request.POST['input_number'] == random_num:
        return render(request, "correct.html")
def too_low(request):
    if request.POST['input_number'] > random_num:
        return render(request,"too_high.html")
def too_high(request):
    if request.POST['input_number'] < random_num:
        return render(request,"too_low.html")
