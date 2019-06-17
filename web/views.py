from django.shortcuts import render
from .forms import TaskForm
from django.http import HttpResponseRedirect
# Create your views here.

# description : This function redners html page and create a form
# author : Saurav Jindal
# returns : render
# Method allowed : GET


def dashboard(request):
    obj = TaskForm()
    return render(request, "index.html ", {"forms":obj})

# description : This function creates task
# author : Saurav Jindal
# returns : HTTP Redirect
# Method allowed : POST, GET#


def CreateTask(request):
    data = TaskForm(request.POST)
    data.save()
    return HttpResponseRedirect('/dashboard')




