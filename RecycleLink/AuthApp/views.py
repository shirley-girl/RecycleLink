from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import messages
from .forms import UserForm, UserProfileForm

# Create your views here.


@login_required(login_url='login')
def profile(request):
    user_profile = request.user.userprofile

    context = {
        'user': request.user,
        'profile': user_profile,
    }
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
            message.error("User does not exists!")
        
        user = authenticate(request, username= username, password = password)

        if user is not None: 
            login(request, user)
            return redirect('dashboard')
        else:
            message.error('Wrong Credentials!!')

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

@login_required
def update_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Profile updated Successfully')
            return redirect('profile')  # Replace with your profile page URL name

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'AuthApp/profile_update.html', context)


   
    

