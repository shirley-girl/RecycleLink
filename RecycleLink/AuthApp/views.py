from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages

# Create your views here.


@login_required(login_url='login')
def profile(request):
    
    context = {'user_profile': request.user.userprofile}
    return render(request, 'AuthApp/profile.html', context)


def loginUser(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exists!")
        
        user = authenticate(request, username= username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('dashboard')
        else:
            print('Wrong Credentials!!')

    context ={}
    return render(request,'AuthApp/login_form.html',context)


def logoutUser(request):
    context = {}
    logout(request)  
    messages.info(request, "You have been logged out.")
    return redirect('login')

def registerUser(request):
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = f"@{user.username}" 
            user.save()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
     else:
        form = UserCreationForm()

     return render(request, 'AuthApp/register_form.html', {'form': form})



   
    

