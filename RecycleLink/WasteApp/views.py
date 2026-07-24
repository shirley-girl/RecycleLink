from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WasteRequest
from .forms import WasteRequestForm
from .models import Company

# Create your views here.
def home(request):
    context = {}
    return render(request, 'WasteApp/home.html', context)

@login_required(login_url='login')
def dashboard(request):
    user_requests = WasteRequest.objects.filter(user= request.user).order_by('-created_at')

    total_requests = user_requests.count()
    pending = user_requests.filter(status='pending').count()
    paid = user_requests.filter(status='paid').count()
    collected = user_requests.filter(status='collected').count()


    context = {
        'total_requests': total_requests,
        'pending': pending,
        'paid': paid,
        'collected': collected,
        'requests': user_requests    
    }
    return render(request, 'WasteApp/dashboard.html', context)

def services(request):
    context = {}
    return render(request, 'WasteApp/services.html', context)

@login_required
def request_pickup(request):
    if request.method =='POST':
        form = WasteRequestForm(request.POST)
        if form.is_valid():
            waste_request = form.save(commit=False)
            waste_request.user = request.user # Attach the logged-in user (from AuthApp)
            if waste_request.assigned_company:
                waste_request.status = 'assigned'
            else:
                waste_request.status = 'pending'    
            waste_request.save()
            return redirect('dashboard')
    else:
            form = WasteRequestForm()
    return render(request, 'WasteApp/request_pickup.html', {'form':form})

from django.shortcuts import get_object_or_404

# UPDATE: Edit a request
@login_required
def update_pickup(request, pk):
    pickup = get_object_or_404(WasteRequest, pk=pk, user=request.user)
    
    # Logic: Only allow editing if it hasn't been collected yet
    if pickup.status in ['paid', 'collected']:
        return redirect('dashboard')

    if request.method == 'POST':
        form = WasteRequestForm(request.POST, instance=pickup)
        if form.is_valid():
            pickup = form.save(commit=False)

            if pickup.assigned_company:
                pickup.status = 'assigned'
            else:
                pickup.status = 'pending'
            pickup.save()
            return redirect('dashboard')
    else:
        form = WasteRequestForm(instance=pickup)
    
    return render(request, 'WasteApp/request_pickup.html', {'form': form, 'edit_mode': True})

# DELETE: Cancel a request
@login_required
def delete_pickup(request, pk):
    pickup = get_object_or_404(WasteRequest, pk=pk, user=request.user)
    
    if request.method == 'POST':
        pickup.delete()
        return redirect('dashboard')
        
    return render(request, 'WasteApp/confirm_delete.html', {'pickup': pickup})


# This view shows the list of all companies
def company_list(request):
    # We only want to show companies that are verified
    companies = Company.objects.all()
    
    # Optional: Allow filtering by waste type if the user clicks a button
    waste_filter = request.GET.get('type')
    if waste_filter and waste_filter != 'all' :
        companies = companies.filter(specialization__iexact=waste_filter)

    return render(request, 'WasteApp/company_list.html', {'companies': companies})

# This view shows details for a specific company
def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'WasteApp/company_detail.html', {'company': company})