from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def janghoon(request):
    return render(request, 'janghoon.html')

def janghoon2(request):
    return render(request, 'janghoon2.html')

def kyungpyo(request):
    return render(request, 'kyungpyo.html')
  
def kyuhwa(request):
    return render(request, 'kyuhwa.html')

