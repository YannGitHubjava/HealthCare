from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Waste
from .forms import WasteForm, LoginForm, SignUpForm

def index(request):
    return render(request, 'WasteManagement/index.html')

def user_login(request):

    form = LoginForm()
    message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form['username'].value()
            password = form['password'].value()

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('all_waste')
            else:
                message = 'Enter Correct Password or Username'

    view_data = {'form': form,
                 'message': message}
        
    return render(request, 'WasteManagement/login.html', view_data)

def user_signup(request):

    form = SignUpForm()
    message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            message = 'Something went wrong. Try Again!'


    view_data = {'form': form,
                 'message': message}
    return render(request, 'WasteManagement/signup.html', view_data )

def user_logout(request):
    logout(request)
    return redirect('home')

def base(request):
    #show_all_waste = Waste.objects.all()
    form = WasteForm()
    return render(request, 'WasteManagement/base.html', {'user':request.user})

@login_required(login_url='/waste/login')
def all_waste(request):
    data = None
    user = request.user 
    uuid = user.id

    if Waste.objects.exists():
        user_waste = Waste.objects.filter(user=uuid)
        if user_waste:
            data = user_waste
    view_data = {'data': data}
    return render(request, 'WasteManagement/all_trash.html', view_data)

@login_required(login_url='/waste/login')
def add_waste(request):
    form = WasteForm()
    message = None
    if request.method == 'POST':
        form = WasteForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.user_id = request.user.id
            user.save()
            message = 'Waste was Successfully created!'
        else:
            message = 'Something Went wrong! Try Again!'

    view_data = {'form': form,
                 'message': message}
    return render(request, 'WasteManagement/add_waste.html', view_data)