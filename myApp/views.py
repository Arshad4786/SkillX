from django.shortcuts import redirect, render
from django.conf import settings
from myApp.forms import TalentForm  # Import settings
from .forms import ClientRegistrationForm
from .models import Client, Talent
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import HireRequestForm

def home(request):
    return render(request, 'myApp/base.html')

def register_talent(request):
    if request.method == 'POST':
        form = TalentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home or success page
    else:
        form = TalentForm()
    return render(request, 'myApp/register.html', {'form': form})

def client_register(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user, name=form.cleaned_data['name'], email=form.cleaned_data['email'])
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = ClientRegistrationForm()
    
    return render(request, 'myApp/client_register.html', {'form': form})

def browse_talents(request):
    talents = Talent.objects.filter(approved=True)  # Filter to only approved talents
    return render(request, 'myApp/browse_talents.html', {'talents': talents})



def talent_detail(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)
    return render(request, 'myApp/talent_detail.html', {'talent': talent})

def talent_list(request):
    # Get all talents where 'approved' is True
    talents = Talent.objects.filter(approved=True)
    return render(request, 'myApp/talent_list.html', {'talents': talents})


def hire_request(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)

    if request.method == 'POST':
        form = HireRequestForm(request.POST)
        if form.is_valid():
            # Create hire request instance and save it
            hire_request = form.save(commit=False)
            hire_request.talent = talent  # Assign the selected talent
            hire_request.client = request.user  # Assign the client (logged-in user)
            hire_request.save()
            return redirect('hire_success')
    else:
        form = HireRequestForm()

    return render(request, 'myApp/hire_request.html', {'form': form, 'talent': talent})


from django.shortcuts import render
from .models import Talent

def client_view(request):
    # Fetch only approved talents
    approved_talents = Talent.objects.filter(approved=True)
    return render(request, 'myApp/client.html', {'approved_talents': approved_talents})

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Talent, HireRequest, Client
from .forms import HireRequestForm

@login_required
def send_hire_request(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)

    # Fetch the Client object based on the logged-in user's email
    client = get_object_or_404(Client, email=request.user.email)

    if request.method == "POST":
        form = HireRequestForm(request.POST)
        if form.is_valid():
            # Create a HireRequest instance and assign the client and talent
            hire_request = form.save(commit=False)
            hire_request.client = client  # Assign the client reference
            hire_request.talent = talent  # Assign the talent reference
            hire_request.status = 'pending'  # Set status to 'pending'
            hire_request.save()  # Save the hire request

            # Redirect to the client view (or any other page after submitting the form)
            return redirect('client_view')  # Adjust to the actual redirect URL

    else:
        form = HireRequestForm()

    return render(request, 'myApp/hire_request.html', {'form': form, 'talent': talent})
