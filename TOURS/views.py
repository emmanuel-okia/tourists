from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'home.html')

def service_view(request):
    return render(request,'service.html')


