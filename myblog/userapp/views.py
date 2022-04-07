from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('userapp:login')
    else:
        form = UserRegisterForm()
    return render(request, 'userapp/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'userapp/profile.html')
