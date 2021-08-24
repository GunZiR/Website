from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from register.forms import UpdateForm

# Create your views here.

def index(response, id):
    return render(response, 'main/profile.htm')

def home(response):
    return render(response, 'main/home.htm', {})

def setting(response, id):
    if response.method == 'POST':
        form = UpdateForm(response.POST, instance=response.user)
        
        if form.is_valid():
            form.save()
            return redirect(f'/users/{id}')
        
    else:
        form = UpdateForm(instance=response.user)
        
    return render(response, 'main/setting.htm', {'form':form})