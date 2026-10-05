from django.shortcuts import render, redirect
from .forms import RegisterForms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib.auth.models import User



# Create your views here.
def register(request):
    if request.method != 'POST':
        forms = RegisterForms()
    else:
        forms = RegisterForms(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('patients:patients_dashboard')
    return render(request, 'registration/register.html', {
        'forms':forms
    })
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'invalid user')
            return redirect('accounts:register')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'invalid password')
        else:
            login(request, user)
            if request.user.role == 'patients':
                return redirect('patients:patients_dashboard')
            elif request.user.role == 'doctor':
                return redirect('Doctors:doctors_dashboard')
    return render(request, 'registration/login.html')
    

        

    


