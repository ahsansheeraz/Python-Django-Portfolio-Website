from django.shortcuts import render

def home(request):
    return render(request, 'cor/home.html')

def about(request):
    return render(request, 'cor/about.html')
    
