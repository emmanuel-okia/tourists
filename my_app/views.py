from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def wild_view(request):
    return render(request, 'wild.html')

def warden_view(request):
    return render(request, 'warden.html')


