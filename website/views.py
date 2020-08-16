from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def other(request):
    return render(request, 'website/other.html')
