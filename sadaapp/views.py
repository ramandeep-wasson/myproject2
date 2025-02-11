from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')  # 

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to homepage or another view
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage or another view
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# added profile section to app
def profile_view(request):
    return render(request, 'profile.html')

#added contact section to sadaapp
def contact_view(request):
    return render(request, 'contact.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


