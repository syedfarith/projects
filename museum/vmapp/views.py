from django.shortcuts import render
from django.http import request
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def home(request):
    return render(request,"home.html")
def explore(request):
    return render(request,"explore.html")

def metro(request):
    return render(request, "metro.html")

def british(request):
    return render(request,"british.html")

def louvre(request):
    return render(request, "louvre.html")

def america(request):
    return render(request, "america.html")

def uffizi(request):
    return render(request, "uffizi.html")

@csrf_protect
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Your account is created Successfully...")  
        else:
            return render(request, "Oops something when wrong.Please try again")
    else:
        form = UserForm()
    return render(request, 'signin.html', {'form': form})
