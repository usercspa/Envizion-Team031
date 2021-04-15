from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account Created!')
            return redirect('user-home')
    else:
        form  = SignUpForm()
    return render(request,'users/register.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')