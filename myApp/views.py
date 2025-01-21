from django.shortcuts import redirect, render
from django.conf import settings
from myApp.forms import TalentForm  # Import settings
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