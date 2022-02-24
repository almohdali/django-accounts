from django.shortcuts import redirect, render
from .models import Profile
from .forms import  SignupForm
from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data['username']
            password = form.changed_data['password2']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
        return render(request,'registration/signup.html',
                      {
                        'form':form,
                      })



def profile(request):
    if request.method == 'POST':
        pass
    else:
        pass
        return render(request,'registration/signup.html',{})
