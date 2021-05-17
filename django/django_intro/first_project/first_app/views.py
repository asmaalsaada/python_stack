
# Create your views here.
from django.shortcuts import redirect, render, HttpResponse, render_to_response
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def root(request):
    return HttpResponse("this is blog!")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")
def destory(request, number):
    return redirect('/blog')

