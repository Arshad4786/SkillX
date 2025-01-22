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


# def hire_request(request, talent_id):
#     talent = get_object_or_404(Talent, id=talent_id)

#     if request.method == 'POST':
#         form = HireRequestForm(request.POST)
#         if form.is_valid():
#             # Create hire request instance and save it
#             hire_request = form.save(commit=False)
#             hire_request.talent = talent  # Assign the selected talent
#             hire_request.client = request.user  # Assign the client (logged-in user)
#             hire_request.save()
#             return redirect('hire_success')
#     else:
#         form = HireRequestForm()

#     return render(request, 'myApp/hire_request.html', {'form': form, 'talent': talent})

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Talent
from .forms import HireRequestForm

@login_required(login_url='client_sign_in')  # Replace 'client_sign_in' with the name of your login view
def hire_request(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)

    if request.method == 'POST':
        form = HireRequestForm(request.POST)
        if form.is_valid():
            # Create hire request instance and save it
            hire_request = form.save(commit=False)
            hire_request.talent = talent
            hire_request.client = request.user  # Assign the client (logged-in user)
            hire_request.save()
            messages.success(request, "Hire request sent successfully!")
            return redirect('hire_success')  # Replace with the name of your success page
    else:
        form = HireRequestForm()

    return render(request, 'myApp/hire_request.html', {'form': form, 'talent': talent})




from django.shortcuts import render
from .models import Talent

from .models import Talent

def client_view(request):
    # Filter talents based on approval status
    approved_talents = Talent.objects.filter(approved=True)
    context = {
        'approved_talents': approved_talents,
    }
    return render(request, 'myApp/client.html', context)

# views.py



from django.shortcuts import render, get_object_or_404, redirect
from .models import Talent
from .forms import HireRequestForm
from django.contrib.auth.decorators import login_required

# This view will handle the hire request process
@login_required
def hire_request(request, talent_id):
    talent = get_object_or_404(Talent, id=talent_id)  # Get the selected talent
    if request.method == 'POST':
        form = HireRequestForm(request.POST)
        if form.is_valid():
            # Save the hire request message to the database
            hire_request = form.save(commit=False)
            hire_request.client = request.user  # Link the request to the logged-in user
            hire_request.talent = talent  # Link the request to the selected talent
            hire_request.save()
            return redirect('some_success_page')  # Redirect to a success page after submission
    else:
        form = HireRequestForm()

    return render(request, 'myApp/hire_request.html', {
        'talent': talent,
        'form': form
    })

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import ClientSignInForm
from .forms import ClientSignUpForm

from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import ClientSignInForm
from django.shortcuts import render, redirect

def client_signin(request):
    next_url = request.GET.get('next', '/')  # Default to home if no 'next' parameter

    if request.method == 'POST':
        form = ClientSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(next_url)  # Redirect to the 'next' URL after login
            else:
                # If credentials are invalid, show an error message
                messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = ClientSignInForm()

    return render(request, 'myApp/login.html', {'form': form})



  


def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_signin')  # Redirect to sign-in after successful sign-up
    else:
        form = ClientSignUpForm()
    return render(request, 'myApp/signup.html', {'form': form})
