from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, AddRecordForm
from .models import Record

def home(request):
    records = Record.objects.all()


    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Error in logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})
    
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered")
            return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "Succesfully logged out")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.Success(request, "Login required")
        return redirect(request, 'home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        curr_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=curr_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated record")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "Login required")
        return redirect('home')


    
def delete_record(request, pk):
    if request.user.is_authenticated:
        to_delete = Record.objects.get(id=pk)
        to_delete.delete()
        messages.success(request, "Successfully deleted record")
        return redirect('home')
    else:
        messages.success(request, "Login required")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Successfully added record")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Login required")
        return redirect(request, 'home')
    


