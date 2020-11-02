from django.http import HttpResponse
from django.shortcuts import render 

#GET request that loads the home page 
def index(request):
    return render(request, 'main/home.html')