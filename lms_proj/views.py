from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def home(request):
    return render(request, 'main_proj/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to Log in')
            return redirect ('login')
    else:
        form = UserRegisterForm()
    return render (request,'registration/register.html',{'form':form})

