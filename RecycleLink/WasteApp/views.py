from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context = {}
    return render(request, 'WasteApp/home.html', context)
    
@login_required(login_url='login')
def dashboard(request):
    context = {}
    return render(request, 'WasteApp/dashboard.html', context)
