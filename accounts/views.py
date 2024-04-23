from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import SignUpForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
import hashlib

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            # CustomUser.objects.create(email = email, password = hashed_pw, username = username)
            CustomUser.objects.create(email = email, password = password, username = username)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            # user = CustomUser.objects.filter(username = username, password = hashed_pw).first()
            user = CustomUser.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect('dashboard')
            else:
                return HttpResponse('Login Failed!!')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
    
def home_view(request):
    return render(request, 'accounts\home.html')

def dashboard_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = CustomUser.objects.get(id = user_id)
        return render(request, 'accounts\dashboard.html', {'message': f'Hi dear {user}!!!!'})
    return redirect('home')
    